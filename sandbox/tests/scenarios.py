"""
End-to-End Test Scenarios
"""
import asyncio
import sys
from pathlib import Path

# Add api directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "api"))

from orchestrator import Orchestrator
from models import InsightRequest
from audit_log import AuditLogger


async def scenario_1_authorized_user():
    """
    Scenario 1: Authorized user can view account insights
    User: user1 (Alice Chen)
    Account: ACME001
    Expected: Success, insights returned with citations
    """
    print("\n" + "="*80)
    print("SCENARIO 1: Authorized User Viewing Account Insights")
    print("="*80)
    print("User: user1 (Alice Chen - group-sales-east, group-finance)")
    print("Account: ACME001 (ACME Corporation)")
    print("Expected: Success with insights\n")

    orchestrator = Orchestrator()
    request = InsightRequest(
        question="What are the current risks and opportunities for ACME?",
        detailLevel="summary"
    )

    response, error = await orchestrator.process_insight_request(
        account_id="ACME001",
        user_oid="user1",
        request=request
    )

    if error:
        print(f"❌ ERROR: {error}")
        return False

    print("✅ REQUEST SUCCESSFUL\n")
    print(f"Account: {response.accountName}")
    print(f"Summary: {response.summary[:200]}...\n")

    print("Risks Identified:")
    for risk in response.risks:
        print(f"  • {risk.name}: {risk.score:.1f}/10 - {risk.reason}")
        print(f"    Citations: {risk.citationIds}")

    print("\nOpportunities:")
    for opp in response.opportunities:
        print(f"  • {opp.name}: {opp.score:.1f}/10 - {opp.reason}")

    print("\nRecommended Next Steps:")
    for step in response.nextSteps:
        print(f"  • {step.action}")
        print(f"    Reason: {step.reason}")
        if step.dueDate:
            print(f"    Due: {step.dueDate}")

    print(f"\nCitations Count: {len(response.citations)}")
    for cite in response.citations[:3]:
        print(f"  • [{cite.source}] {cite.text}")
        print(f"    → {cite.sourceUri}")

    return True


async def scenario_2_unauthorized_user():
    """
    Scenario 2: Unauthorized user gets 404 (no permission leak)
    User: user4 (David Lee - group-sales-south only)
    Account: ACME001 (allowed: group-sales-east, group-finance)
    Expected: 404 "Not Found" without revealing permission issue
    """
    print("\n" + "="*80)
    print("SCENARIO 2: Unauthorized User Access Attempt")
    print("="*80)
    print("User: user4 (David Lee - group-sales-south only)")
    print("Account: ACME001 (requires: group-sales-east or group-finance)")
    print("Expected: 404 Not Found (no permission leak)\n")

    orchestrator = Orchestrator()
    request = InsightRequest()

    response, error = await orchestrator.process_insight_request(
        account_id="ACME001",
        user_oid="user4",
        request=request
    )

    if response is not None:
        print("❌ FAILED: Should have returned error")
        return False

    if error == "Not Found":
        print("✅ ACCESS DENIED - Correct error message (no permission leak)")
        print(f"Error: {error}")
        return True
    else:
        print(f"❌ FAILED: Wrong error message: {error}")
        return False


async def scenario_3_audit_logging():
    """
    Scenario 3: Audit logging verification
    Verify that all queries and access decisions are logged
    """
    print("\n" + "="*80)
    print("SCENARIO 3: Audit Logging Verification")
    print("="*80)

    orchestrator = Orchestrator()

    # Clear audit log for clean test
    audit_log_path = Path(".copilot-tracking/audit_log_test.jsonl")
    orchestrator.audit_logger.log_file = audit_log_path

    # Make authorized request
    request = InsightRequest()
    response1, _ = await orchestrator.process_insight_request(
        account_id="ACME001",
        user_oid="user1",
        request=request
    )

    # Make unauthorized request
    response2, _ = await orchestrator.process_insight_request(
        account_id="ACME001",
        user_oid="user4",
        request=request
    )

    # Check audit logs
    logs = orchestrator.audit_logger.get_logs()
    print(f"\nTotal Audit Events: {len(logs)}")

    print("\nRecent Events:")
    for i, log in enumerate(logs[:5]):
        print(f"  {i+1}. [{log.eventType}] {log.userId} @ {log.timestamp}")
        if log.status:
            print(f"     Status: {log.status}")
        if log.accountId:
            print(f"     Account: {log.accountId}")

    # Verify we have both success and denied events
    has_success = any(log.eventType == "query_answered" for log in logs)
    has_denied = any(log.eventType == "access_denied" for log in logs)

    if has_success and has_denied:
        print("\n✅ AUDIT LOGGING VERIFIED")
        print("   • query_answered events recorded")
        print("   • access_denied events recorded")
        return True
    else:
        print("\n❌ AUDIT LOGGING INCOMPLETE")
        return False


async def scenario_4_citation_validation():
    """
    Scenario 4: Citation validation
    Verify that citations are properly linked to facts
    """
    print("\n" + "="*80)
    print("SCENARIO 4: Citation Validation")
    print("="*80)

    orchestrator = Orchestrator()
    request = InsightRequest(question="What is the financial status?")

    response, error = await orchestrator.process_insight_request(
        account_id="TECH002",
        user_oid="user2",
        request=request
    )

    if error:
        print(f"❌ ERROR: {error}")
        return False

    print(f"Response Summary: {response.summary[:250]}...\n")
    print(f"Citations Provided: {len(response.citations)}\n")

    # Verify citations exist and have required fields
    all_valid = True
    for i, cite in enumerate(response.citations):
        print(f"Citation {i+1}:")
        print(f"  Text: {cite.text[:80]}")
        print(f"  Source: {cite.source}")
        print(f"  URI: {cite.sourceUri}")
        print(f"  Confidence: {cite.confidence:.0%}\n")

        if not cite.sourceUri or not cite.source:
            all_valid = False

    if all_valid:
        print("✅ CITATIONS VALIDATED")
        return True
    else:
        print("❌ CITATION VALIDATION FAILED")
        return False


async def scenario_5_different_accounts():
    """
    Scenario 5: Test different account scenarios
    - ACME001: At risk (revenue decline)
    - TECH002: Growth opportunity (expansion)
    - FINANCE003: Strategic partnership
    """
    print("\n" + "="*80)
    print("SCENARIO 5: Different Account Profiles")
    print("="*80)

    orchestrator = Orchestrator()
    request = InsightRequest()

    accounts = [
        ("ACME001", "user1", "ACME - At Risk Profile"),
        ("TECH002", "user2", "TechVision - Growth Profile"),
        ("FINANCE003", "user3", "FinanceHub - Strategic Profile"),
    ]

    all_passed = True
    for account_id, user_oid, description in accounts:
        print(f"\n{description}")
        print(f"  Account: {account_id}, User: {user_oid}")

        response, error = await orchestrator.process_insight_request(
            account_id=account_id,
            user_oid=user_oid,
            request=request
        )

        if error:
            print(f"  ❌ ERROR: {error}")
            all_passed = False
            continue

        print(f"  ✅ Success")
        print(f"    Risks: {len(response.risks)}")
        print(f"    Opportunities: {len(response.opportunities)}")
        print(f"    Citations: {len(response.citations)}")

        if response.risks:
            top_risk = max(response.risks, key=lambda x: x.score)
            print(f"    Top Risk: {top_risk.name} ({top_risk.score:.1f}/10)")

        if response.opportunities:
            top_opp = max(response.opportunities, key=lambda x: x.score)
            print(f"    Top Opportunity: {top_opp.name} ({top_opp.score:.1f}/10)")

    return all_passed


async def main():
    """Run all scenarios"""
    print("\n" + "="*80)
    print("RM INTELLIGENCE EXPERIENCE - END-TO-END SANDBOX SIMULATION")
    print("="*80)

    results = []

    # Run scenarios
    results.append(("Scenario 1: Authorized User", await scenario_1_authorized_user()))
    results.append(("Scenario 2: Unauthorized User", await scenario_2_unauthorized_user()))
    results.append(("Scenario 3: Audit Logging", await scenario_3_audit_logging()))
    results.append(("Scenario 4: Citation Validation", await scenario_4_citation_validation()))
    results.append(("Scenario 5: Account Profiles", await scenario_5_different_accounts()))

    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name}: {status}")

    passed_count = sum(1 for _, p in results if p)
    total_count = len(results)
    print(f"\nTotal: {passed_count}/{total_count} scenarios passed")

    return passed_count == total_count


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
