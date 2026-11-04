"""
Audit Log Service: Immutable audit trail
"""
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from models import AuditLogEvent


class AuditLogger:
    """
    Immutable audit logging service.
    All events are appended to a log file.
    """

    def __init__(self, log_file: str = ".copilot-tracking/audit_log.jsonl"):
        self.log_file = Path(log_file)
        # Create parent directory if needed
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def log_event(self, event: AuditLogEvent) -> None:
        """
        Append event to audit log.
        Uses JSONL format (one JSON object per line).
        """
        with open(self.log_file, "a") as f:
            f.write(json.dumps(event.model_dump()) + "\n")

    def log_query_answered(
        self,
        user_id: str,
        account_id: str,
        correlation_id: str,
        citation_ids: List[str],
        summary: str
    ) -> None:
        """Log successful query response"""
        event = AuditLogEvent(
            timestamp=datetime.utcnow().isoformat() + "Z",
            eventType="query_answered",
            userId=user_id,
            correlationId=correlation_id,
            accountId=account_id,
            citationIds=citation_ids,
            resultSummary=summary,
            status="success"
        )
        self.log_event(event)

    def log_access_denied(
        self,
        user_id: str,
        account_id: str,
        correlation_id: str,
        reason: str
    ) -> None:
        """Log access denied event"""
        event = AuditLogEvent(
            timestamp=datetime.utcnow().isoformat() + "Z",
            eventType="access_denied",
            userId=user_id,
            correlationId=correlation_id,
            accountId=account_id,
            citationIds=[],
            resultSummary=None,
            status="denied",
            details={"reason": reason}
        )
        self.log_event(event)

    def log_search_executed(
        self,
        user_id: str,
        correlation_id: str,
        account_id: Optional[str],
        query: str,
        result_count: int
    ) -> None:
        """Log search execution"""
        event = AuditLogEvent(
            timestamp=datetime.utcnow().isoformat() + "Z",
            eventType="search_executed",
            userId=user_id,
            correlationId=correlation_id,
            accountId=account_id,
            citationIds=[],
            resultSummary=f"Search returned {result_count} results",
            status="success",
            details={"query": query, "result_count": result_count}
        )
        self.log_event(event)

    def log_token_validation_failed(
        self,
        correlation_id: str,
        reason: str
    ) -> None:
        """Log authentication failure"""
        event = AuditLogEvent(
            timestamp=datetime.utcnow().isoformat() + "Z",
            eventType="auth_failed",
            userId="unknown",
            correlationId=correlation_id,
            accountId=None,
            citationIds=[],
            resultSummary=None,
            status="error",
            details={"reason": reason}
        )
        self.log_event(event)

    def log_error(
        self,
        user_id: str,
        correlation_id: str,
        error_msg: str,
        account_id: Optional[str] = None
    ) -> None:
        """Log application error"""
        event = AuditLogEvent(
            timestamp=datetime.utcnow().isoformat() + "Z",
            eventType="error",
            userId=user_id,
            correlationId=correlation_id,
            accountId=account_id,
            citationIds=[],
            resultSummary=None,
            status="error",
            details={"error": error_msg}
        )
        self.log_event(event)

    def get_logs(
        self,
        event_type: Optional[str] = None,
        user_id: Optional[str] = None,
        account_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100
    ) -> List[AuditLogEvent]:
        """
        Query audit logs.
        
        Args:
            event_type: Filter by event type
            user_id: Filter by user
            account_id: Filter by account
            start_date: ISO format start date
            end_date: ISO format end date
            limit: Max results
        
        Returns:
            List of matching events
        """
        if not self.log_file.exists():
            return []

        events = []
        with open(self.log_file, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    event = AuditLogEvent(**data)

                    # Apply filters
                    if event_type and event.eventType != event_type:
                        continue
                    if user_id and event.userId != user_id:
                        continue
                    if account_id and event.accountId != account_id:
                        continue
                    if start_date and event.timestamp < start_date:
                        continue
                    if end_date and event.timestamp > end_date:
                        continue

                    events.append(event)
                except json.JSONDecodeError:
                    continue

        # Return most recent first
        events.sort(key=lambda x: x.timestamp, reverse=True)
        return events[:limit]

    def get_statistics(self) -> Dict[str, Any]:
        """Get audit log statistics"""
        if not self.log_file.exists():
            return {"total_events": 0, "by_type": {}, "by_user": {}}

        total_events = 0
        by_type = {}
        by_user = {}
        by_status = {}

        with open(self.log_file, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    total_events += 1

                    event_type = data.get("eventType", "unknown")
                    by_type[event_type] = by_type.get(event_type, 0) + 1

                    user_id = data.get("userId", "unknown")
                    by_user[user_id] = by_user.get(user_id, 0) + 1

                    status = data.get("status", "unknown")
                    by_status[status] = by_status.get(status, 0) + 1
                except json.JSONDecodeError:
                    continue

        return {
            "total_events": total_events,
            "by_type": by_type,
            "by_user": by_user,
            "by_status": by_status
        }
