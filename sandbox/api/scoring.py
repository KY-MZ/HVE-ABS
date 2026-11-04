"""
Scoring Engine: Deterministic risk and opportunity calculation
"""
import json
from pathlib import Path
from typing import Dict, Tuple, List, Any
from datetime import datetime
from dateutil import parser as date_parser


class ScoringEngine:
    """
    Deterministic scoring for risk and opportunity indicators.
    All calculations are rule-based (no ML models).
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.transactions_cache = self._load_transactions()
        self.accounts_cache = self._load_accounts()
        self.emails_cache = self._load_emails()

    def _load_transactions(self) -> Dict[str, List[Dict]]:
        """Load transactions grouped by account"""
        txns_file = self.data_dir / "transactions.json"
        with open(txns_file) as f:
            transactions = json.load(f)

        by_account = {}
        for txn in transactions:
            account_id = txn["accountId"]
            if account_id not in by_account:
                by_account[account_id] = []
            by_account[account_id].append(txn)

        return by_account

    def _load_accounts(self) -> Dict[str, Dict]:
        """Load accounts"""
        accounts_file = self.data_dir / "accounts.json"
        with open(accounts_file) as f:
            accounts = json.load(f)
        return {acc["id"]: acc for acc in accounts}

    def _load_emails(self) -> Dict[str, List[Dict]]:
        """Load emails grouped by account"""
        emails_file = self.data_dir / "emails.json"
        with open(emails_file) as f:
            emails = json.load(f)

        by_account = {}
        for email in emails:
            account_id = email["accountId"]
            if account_id not in by_account:
                by_account[account_id] = []
            by_account[account_id].append(email)

        return by_account

    def calculate_risk_scores(self, account_id: str) -> Dict[str, Tuple[float, str, List[str]]]:
        """
        Calculate risk scores for an account.
        
        Returns:
            Dict of { risk_name: (score: 0-10, reason: str, citation_ids: List[str]) }
        """
        risks = {}

        # Risk 1: Revenue Decline
        revenue_decline_score, reason, citations = self._calculate_revenue_decline_risk(account_id)
        if revenue_decline_score > 0:
            risks["Revenue Decline"] = (revenue_decline_score, reason, citations)

        # Risk 2: Engagement Decline
        engagement_score, reason, citations = self._calculate_engagement_risk(account_id)
        if engagement_score > 0:
            risks["Engagement Decline"] = (engagement_score, reason, citations)

        # Risk 3: Account Status
        status_score, reason, citations = self._calculate_status_risk(account_id)
        if status_score > 0:
            risks["Account Status"] = (status_score, reason, citations)

        return risks

    def calculate_opportunity_scores(self, account_id: str) -> Dict[str, Tuple[float, str, List[str]]]:
        """
        Calculate opportunity scores for an account.
        
        Returns:
            Dict of { opportunity_name: (score: 0-10, reason: str, citation_ids: List[str]) }
        """
        opportunities = {}

        # Opportunity 1: Growth Expansion
        expansion_score, reason, citations = self._calculate_expansion_opportunity(account_id)
        if expansion_score > 0:
            opportunities["Growth Expansion"] = (expansion_score, reason, citations)

        # Opportunity 2: Strategic Partnership
        partnership_score, reason, citations = self._calculate_partnership_opportunity(account_id)
        if partnership_score > 0:
            opportunities["Strategic Partnership"] = (partnership_score, reason, citations)

        # Opportunity 3: Service Enhancement
        enhancement_score, reason, citations = self._calculate_enhancement_opportunity(account_id)
        if enhancement_score > 0:
            opportunities["Service Enhancement"] = (enhancement_score, reason, citations)

        return opportunities

    # ========================================================================
    # Risk Calculators
    # ========================================================================

    def _calculate_revenue_decline_risk(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Detect revenue decline trend.
        Rule: If transaction average decreased >15% in last 2 months vs prior 2 months.
        """
        txns = self.transactions_cache.get(account_id, [])
        if len(txns) < 2:
            return 0.0, "", []

        # Sort by date
        sorted_txns = sorted(txns, key=lambda x: x["date"], reverse=True)

        # Split into recent (last 2) and prior (prev 2)
        recent = sorted_txns[:2]
        prior = sorted_txns[2:4] if len(sorted_txns) >= 4 else []

        if not prior:
            return 0.0, "", []

        recent_avg = sum(t["amount"] for t in recent) / len(recent)
        prior_avg = sum(t["amount"] for t in prior) / len(prior)

        decline_pct = (prior_avg - recent_avg) / prior_avg * 100

        if decline_pct >= 15:
            score = min(decline_pct / 10, 10.0)  # Scale to 0-10
            citations = [t["sourceUri"] for t in recent + prior]
            reason = f"Transaction volume declined {decline_pct:.0f}% (from ${prior_avg:,.0f} to ${recent_avg:,.0f})"
            return score, reason, citations

        return 0.0, "", []

    def _calculate_engagement_risk(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Detect engagement decline.
        Rule: If email communication decreased significantly or recent emails show concerns.
        """
        emails = self.emails_cache.get(account_id, [])
        if len(emails) < 2:
            return 0.0, "", []

        # Check for concern keywords in recent emails
        recent_emails = sorted(emails, key=lambda x: x["date"], reverse=True)[:2]
        concern_keywords = ["budget", "concerns", "issues", "decline", "constraints", "delayed"]

        citations = []
        concern_count = 0

        for email in recent_emails:
            body_lower = email["body"].lower()
            for keyword in concern_keywords:
                if keyword in body_lower:
                    concern_count += 1
                    citations.append(email["sourceUri"])
                    break

        if concern_count > 0:
            score = min(concern_count * 3.5, 8.0)
            reason = f"Recent communications indicate potential concerns ({concern_count} engagement issue(s) detected)"
            return score, reason, citations

        # Check frequency decline
        if len(emails) >= 4:
            sorted_emails = sorted(emails, key=lambda x: x["date"])
            recent_frequency = len([e for e in sorted_emails[-2:]])
            prior_frequency = len([e for e in sorted_emails[-4:-2]])

            if prior_frequency > recent_frequency:
                score = 4.0
                reason = "Email communication frequency has decreased"
                citations = [e["sourceUri"] for e in sorted_emails[-4:]]
                return score, reason, citations

        return 0.0, "", []

    def _calculate_status_risk(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Check account status field.
        """
        account = self.accounts_cache.get(account_id)
        if not account:
            return 0.0, "", []

        if account.get("status") == "At Risk":
            reason = f"Account marked as '{account['status']}' status"
            return 6.5, reason, []

        return 0.0, "", []

    # ========================================================================
    # Opportunity Calculators
    # ========================================================================

    def _calculate_expansion_opportunity(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Detect expansion opportunities from emails mentioning growth plans.
        """
        emails = self.emails_cache.get(account_id, [])
        growth_keywords = ["expand", "growth", "increase", "hiring", "headcount", "venture", "funding"]
        citations = []

        for email in emails:
            body_lower = email["body"].lower()
            if any(keyword in body_lower for keyword in growth_keywords):
                citations.append(email["sourceUri"])

        if citations:
            score = min(len(citations) * 3.0, 9.0)
            reason = f"Client shows growth indicators ({len(citations)} mention(s) of expansion/growth)"
            return score, reason, citations

        return 0.0, "", []

    def _calculate_partnership_opportunity(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Detect strategic partnership opportunities.
        """
        emails = self.emails_cache.get(account_id, [])
        partnership_keywords = ["partnership", "strategic", "expansion", "asia", "advisory", "consulting"]
        citations = []

        for email in emails:
            body_lower = email["body"].lower()
            if any(keyword in body_lower for keyword in partnership_keywords):
                citations.append(email["sourceUri"])

        if citations:
            score = min(len(citations) * 2.5, 8.5)
            reason = f"Strategic partnership potential identified ({len(citations)} indicator(s))"
            return score, reason, citations

        return 0.0, "", []

    def _calculate_enhancement_opportunity(self, account_id: str) -> Tuple[float, str, List[str]]:
        """
        Detect service enhancement opportunities.
        """
        emails = self.emails_cache.get(account_id, [])
        # Look for mentions of service issues that could be improvement opportunities
        service_keywords = ["support", "quality", "service", "resource", "help", "improve"]
        citations = []

        for email in emails:
            body_lower = email["body"].lower()
            # Look for combination: service + positive engagement
            if "support" in body_lower and ("team" in body_lower or "resource" in body_lower):
                citations.append(email["sourceUri"])

        if citations:
            score = 5.5
            reason = f"Service enhancement and support improvement opportunity"
            return score, reason, citations

        return 0.0, "", []
