"""
Orchestrator: Main coordination logic for insight generation
"""
import json
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime

from models import (
    UserContext, InsightRequest, InsightResponse, Citation,
    RiskIndicator, Opportunity, NextStep, AuditLogEvent
)
from identity_service import IdentityService
from search_service import SearchService
from scoring import ScoringEngine
from llm_service import LLMMock
from audit_log import AuditLogger


class Orchestrator:
    """
    Main orchestration logic:
    1. Validate access (ACL)
    2. Search for evidence
    3. Calculate scores
    4. Generate text via LLM
    5. Validate citations
    6. Log audit trail
    """

    def __init__(self, data_dir: str = "data", log_file: str = ".copilot-tracking/audit_log.jsonl"):
        self.identity_service = IdentityService(data_dir)
        self.search_service = SearchService(data_dir)
        self.scoring_engine = ScoringEngine(data_dir)
        self.llm_service = LLMMock()
        self.audit_logger = AuditLogger(log_file)
        self.data_dir = Path(data_dir)

    async def process_insight_request(
        self,
        account_id: str,
        user_oid: str,
        request: InsightRequest
    ) -> Tuple[Optional[InsightResponse], Optional[str]]:
        """
        Process insight request end-to-end.
        
        Returns:
            (InsightResponse, error_message)
            - If error_message is not None, InsightResponse will be None
        """

        # ====================================================================
        # Phase 1: Create user context and validate token
        # ====================================================================
        user_context = self.identity_service.create_user_context_from_token(user_oid)
        if not user_context:
            self.audit_logger.log_token_validation_failed(
                "unknown",
                f"Invalid user OID: {user_oid}"
            )
            return None, "Unauthorized: Invalid user token"

        # ====================================================================
        # Phase 2: Check account access (ACL)
        # ====================================================================
        access_result = self.identity_service.check_account_access(
            account_id,
            user_context
        )

        if not access_result.allowed:
            self.audit_logger.log_access_denied(
                user_context.oid,
                account_id,
                user_context.correlationId,
                access_result.reason or "Access denied"
            )
            return None, f"Not Found"  # Don't reveal permission reason

        # ====================================================================
        # Phase 3: Load account data
        # ====================================================================
        account = self._load_account(account_id)
        if not account:
            self.audit_logger.log_access_denied(
                user_context.oid,
                account_id,
                user_context.correlationId,
                "Account not found"
            )
            return None, "Not Found"

        # ====================================================================
        # Phase 4: Search for evidence
        # ====================================================================
        search_results = self.search_service.search(
            query=request.question or f"{account['name']} account",
            account_id=account_id,
            user_groups=user_context.groups,
            limit=20
        )

        self.audit_logger.log_search_executed(
            user_context.oid,
            user_context.correlationId,
            account_id,
            request.question or "",
            len(search_results)
        )

        # ====================================================================
        # Phase 5: Calculate risk & opportunity scores
        # ====================================================================
        risk_scores = self.scoring_engine.calculate_risk_scores(account_id)
        opportunity_scores = self.scoring_engine.calculate_opportunity_scores(account_id)

        # ====================================================================
        # Phase 6: Generate response via LLM Mock
        # ====================================================================
        (
            summary_text,
            used_citation_ids,
            risks_output,
            opps_output,
            next_steps_output
        ) = self.llm_service.generate_insight_response(
            account["name"],
            risk_scores,
            opportunity_scores,
            [r.model_dump() for r in search_results],
            {}
        )

        # ====================================================================
        # Phase 7: Build citations
        # ====================================================================
        citations = self._build_citations(used_citation_ids, search_results)

        # ====================================================================
        # Phase 8: Remove uncited sentences (validation)
        # ====================================================================
        validated_summary = self._validate_citations(
            summary_text,
            citations
        )

        # ====================================================================
        # Phase 9: Build response
        # ====================================================================
        response = InsightResponse(
            accountId=account_id,
            accountName=account["name"],
            summary=validated_summary,
            risks=[
                RiskIndicator(
                    name=r["name"],
                    score=r["score"],
                    reason=r["reason"],
                    citationIds=r.get("citationIds", [])
                )
                for r in risks_output
            ],
            opportunities=[
                Opportunity(
                    name=o["name"],
                    score=o["score"],
                    reason=o["reason"],
                    citationIds=o.get("citationIds", [])
                )
                for o in opps_output
            ],
            nextSteps=[
                NextStep(
                    action=s["action"],
                    owner=s.get("owner"),
                    dueDate=s.get("dueDate"),
                    reason=s["reason"],
                    citationIds=s.get("citationIds", [])
                )
                for s in next_steps_output
            ],
            citations=citations,
            generatedAt=datetime.utcnow().isoformat() + "Z"
        )

        # ====================================================================
        # Phase 10: Log audit trail
        # ====================================================================
        self.audit_logger.log_query_answered(
            user_context.oid,
            account_id,
            user_context.correlationId,
            used_citation_ids,
            validated_summary[:100]  # First 100 chars
        )

        return response, None

    def _load_account(self, account_id: str) -> Optional[Dict]:
        """Load account from data"""
        accounts_file = self.data_dir / "accounts.json"
        with open(accounts_file) as f:
            accounts = json.load(f)
        for acc in accounts:
            if acc["id"] == account_id:
                return acc
        return None

    def _build_citations(
        self,
        used_citation_ids: List[str],
        search_results: List[Any]
    ) -> List[Citation]:
        """
        Build citation list from used citation IDs.
        Map citation IDs to search result documents.
        """
        citations = []
        citation_map = {r.id: r for r in search_results}

        for cite_id in used_citation_ids:
            if cite_id in citation_map:
                result = citation_map[cite_id]
                # Infer citation text from document content
                text = self._extract_citation_text(result)
                citation = Citation(
                    text=text,
                    sourceUri=result.sourceUri,
                    confidence=result.score or 0.85,
                    source=result.source
                )
                citations.append(citation)

        return citations

    def _extract_citation_text(self, result: Any) -> str:
        """Extract representative text from search result"""
        # Use title as citation text if available
        if hasattr(result, 'title') and result.title:
            return result.title
        if hasattr(result, 'content') and result.content:
            return result.content[:100].strip() + "..."
        return "Document reference"

    def _validate_citations(
        self,
        summary_text: str,
        citations: List[Citation]
    ) -> str:
        """
        Validate that sentences in summary have citations.
        For now, returns text as-is (in real scenario would parse and validate).
        """
        # Simplified validation - in production would parse actual citation markers
        return summary_text

    def get_audit_stats(self) -> Dict[str, Any]:
        """Get audit log statistics"""
        return self.audit_logger.get_statistics()

    def get_user_audit_logs(
        self,
        user_oid: str,
        limit: int = 50
    ) -> List[Dict]:
        """Get audit logs for a user"""
        logs = self.audit_logger.get_logs(user_id=user_oid, limit=limit)
        return [log.model_dump() for log in logs]

    def get_account_audit_logs(
        self,
        account_id: str,
        limit: int = 50
    ) -> List[Dict]:
        """Get audit logs for an account"""
        logs = self.audit_logger.get_logs(account_id=account_id, limit=limit)
        return [log.model_dump() for log in logs]
