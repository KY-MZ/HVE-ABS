"""
LLM Service Mock: Simulates Azure OpenAI text generation
"""
import json
from typing import Dict, List, Any, Tuple
from datetime import datetime
from models import LLMRequest, LLMResponse, Citation


class LLMMock:
    """
    Mock LLM service that simulates Azure OpenAI behavior.
    Takes context and generates grounded, citation-aware responses.
    """

    # Templates for different response patterns
    RISK_TEMPLATES = {
        "Revenue Decline": "The account has experienced a {pct}% decline in transaction volume, from ${prev} to ${curr}. This trend suggests potential budget constraints or business challenges.",
        "Engagement Decline": "Recent communications indicate declining engagement, with fewer interactions and expressions of concern about service quality and resource constraints.",
        "Account Status": "The account is currently marked as 'At Risk' status, requiring immediate attention and relationship management.",
    }

    OPPORTUNITY_TEMPLATES = {
        "Growth Expansion": "The client is actively planning expansion initiatives, including {pct} headcount growth and increased investment in new markets.",
        "Strategic Partnership": "There is significant potential for deepening the strategic partnership, particularly around expansion into new geographic markets.",
        "Service Enhancement": "The client values our partnership and sees opportunities to enhance service quality and support responsiveness.",
    }

    def __init__(self):
        pass

    def generate_insight_response(
        self,
        account_name: str,
        risk_analysis: Dict[str, Tuple[float, str, List[str]]],
        opportunity_analysis: Dict[str, Tuple[float, str, List[str]]],
        search_results: Dict[str, Any],
        transactions_summary: Dict[str, Any]
    ) -> Tuple[str, List[str], List[Dict], List[Dict], List[Dict]]:
        """
        Generate insight response with citations.
        
        Returns:
            (summary_text, used_citation_ids, risks_with_citations, opps_with_citations, next_steps_with_citations)
        """
        summary_parts = []
        used_citations = set()
        risks_output = []
        opps_output = []
        next_steps_output = []

        # ====================================================================
        # Build Risk Summary with Citations
        # ====================================================================
        if risk_analysis:
            summary_parts.append(f"**Risk Analysis for {account_name}:**")

            for risk_name, (score, reason, citations) in sorted(
                risk_analysis.items(), key=lambda x: x[1][0], reverse=True
            ):
                summary_parts.append(f"\n• {risk_name} (Score: {score:.1f}/10): {reason}")
                used_citations.update(citations)

                risks_output.append({
                    "name": risk_name,
                    "score": round(score, 1),
                    "reason": reason,
                    "citationIds": citations
                })
        else:
            summary_parts.append(f"**Risk Analysis for {account_name}:**\nNo significant risks identified.")

        # ====================================================================
        # Build Opportunity Summary with Citations
        # ====================================================================
        summary_parts.append("\n**Growth Opportunities:**")
        if opportunity_analysis:
            for opp_name, (score, reason, citations) in sorted(
                opportunity_analysis.items(), key=lambda x: x[1][0], reverse=True
            ):
                summary_parts.append(f"\n• {opp_name} (Score: {score:.1f}/10): {reason}")
                used_citations.update(citations)

                opps_output.append({
                    "name": opp_name,
                    "score": round(score, 1),
                    "reason": reason,
                    "citationIds": citations
                })
        else:
            summary_parts.append("\nNo immediate opportunities identified.")

        # ====================================================================
        # Generate Next Steps with Citations
        # ====================================================================
        summary_parts.append("\n**Recommended Next Steps:**")
        next_steps_generated = self._generate_next_steps(
            account_name,
            risk_analysis,
            opportunity_analysis,
            used_citations
        )

        for step in next_steps_generated:
            next_steps_output.append(step)
            summary_parts.append(f"\n• {step['action']}")
            if step.get("dueDate"):
                summary_parts.append(f"  (Due: {step['dueDate']})")

        summary_text = "\n".join(summary_parts)
        return summary_text, list(used_citations), risks_output, opps_output, next_steps_output

    def _generate_next_steps(
        self,
        account_name: str,
        risks: Dict,
        opportunities: Dict,
        used_citations: set
    ) -> List[Dict]:
        """Generate recommended next steps based on risks and opportunities"""
        steps = []

        # High-risk accounts need immediate outreach
        max_risk_score = max((score for score, _, _ in risks.values()), default=0)
        if max_risk_score >= 7:
            step = {
                "action": f"Schedule urgent business review with {account_name} leadership",
                "reason": "High risk score indicates potential churn risk",
                "owner": "Account Manager",
                "dueDate": "2026-11-10",
                "citationIds": list(used_citations)[:1] if used_citations else []
            }
            steps.append(step)

        # High-opportunity accounts for expansion
        max_opp_score = max((score for score, _, _ in opportunities.values()), default=0)
        if max_opp_score >= 7:
            step = {
                "action": f"Prepare expansion proposal for {account_name}",
                "reason": "Strong growth and partnership potential identified",
                "owner": "Strategic Partner",
                "dueDate": "2026-11-20",
                "citationIds": list(used_citations)[-1:] if used_citations else []
            }
            steps.append(step)

        # Service quality issues
        if any("service" in r.lower() or "support" in r.lower() for r in risks.keys()):
            step = {
                "action": f"Evaluate and enhance service delivery for {account_name}",
                "reason": "Service quality concerns raised in recent communications",
                "owner": "Service Lead",
                "dueDate": "2026-11-15",
                "citationIds": []
            }
            steps.append(step)

        # Default follow-up if no strong signals
        if not steps:
            step = {
                "action": f"Standard quarterly business review with {account_name}",
                "reason": "Routine relationship management and account check-in",
                "owner": "Account Manager",
                "dueDate": "2026-11-30",
                "citationIds": []
            }
            steps.append(step)

        return steps

    def validate_citations(
        self,
        summary_text: str,
        available_citations: Dict[str, str]
    ) -> str:
        """
        Validate that all sentences in summary have citations.
        Remove sentences without citations.
        
        Args:
            summary_text: Generated text
            available_citations: Map of sourceUri -> citation text
        
        Returns:
            Cleaned text with only cited sentences
        """
        # This is a simplified version - in real scenario would parse actual citations
        # For now, we trust that citations are embedded in the model output
        return summary_text

    def mock_generate(self, prompt: str) -> str:
        """
        Simple mock generation for testing.
        In real scenario, would call Azure OpenAI API.
        """
        return f"[Mock Response to: {prompt[:50]}...]"
