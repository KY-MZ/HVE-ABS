"""
FastAPI Main Application
RM Intelligence Experience Sandbox
"""
from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from typing import Optional, List
import uuid

from models import (
    InsightRequest, InsightResponse, AuditLogEvent
)
from orchestrator import Orchestrator

# ============================================================================
# Initialize
# ============================================================================
app = FastAPI(
    title="RM Intelligence Experience API",
    description="Relationship Manager Intelligence Experience Sandbox",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator
orchestrator = Orchestrator(data_dir="data")

# ============================================================================
# Middleware & Utilities
# ============================================================================

@app.middleware("http")
async def add_correlation_id(request, call_next):
    """Add correlation ID to all requests"""
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = correlation_id
    return response


def extract_user_oid(authorization: Optional[str]) -> Optional[str]:
    """
    Extract user OID from Authorization header.
    Format: Bearer <user_oid>
    In real scenario, would validate JWT token against Entra.
    """
    if not authorization:
        return None
    parts = authorization.split()
    if len(parts) != 2 or parts[0] != "Bearer":
        return None
    return parts[1]


# ============================================================================
# Health Check
# ============================================================================

@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "RM Intelligence Experience API",
        "version": "0.1.0"
    }


# ============================================================================
# Main API Endpoints
# ============================================================================

@app.post(
    "/api/v1/accounts/{account_id}/insights",
    response_model=InsightResponse,
    tags=["Insights"]
)
async def get_account_insights(
    account_id: str,
    request: InsightRequest,
    authorization: Optional[str] = Header(None),
    x_correlation_id: Optional[str] = Header(None)
):
    """
    Get insights for an account.
    
    Request body:
    - question: Optional question about the account
    - detailLevel: "summary" or "detailed"
    
    Returns:
    - Insight response with risks, opportunities, next steps, and citations
    """
    # Extract user from token
    user_oid = extract_user_oid(authorization)
    if not user_oid:
        raise HTTPException(status_code=401, detail="Unauthorized: Missing or invalid token")

    # Process request
    response, error = await orchestrator.process_insight_request(
        account_id=account_id,
        user_oid=user_oid,
        request=request
    )

    if error:
        if error == "Not Found":
            raise HTTPException(status_code=404, detail="Account not found")
        raise HTTPException(status_code=500, detail=error)

    return response


@app.get(
    "/api/v1/search",
    tags=["Search"]
)
async def search(
    q: str = Query(..., description="Search query"),
    account_id: Optional[str] = Query(None, description="Limit to specific account"),
    limit: int = Query(10, ge=1, le=100),
    authorization: Optional[str] = Header(None)
):
    """
    Search across data sources with ACL filtering.
    """
    user_oid = extract_user_oid(authorization)
    if not user_oid:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Get user context
    user_context = orchestrator.identity_service.create_user_context_from_token(user_oid)
    if not user_context:
        raise HTTPException(status_code=401, detail="Invalid user")

    # Get allowed accounts
    allowed_accounts = orchestrator.identity_service.get_user_allowed_accounts(user_context)

    # Perform search
    results = orchestrator.search_service.search(
        query=q,
        account_id=account_id,
        allowed_accounts=allowed_accounts,
        user_groups=user_context.groups,
        limit=limit
    )

    return {
        "query": q,
        "results": [r.model_dump() for r in results],
        "total": len(results),
        "filtered_by_acl": True
    }


@app.get(
    "/api/v1/audit-logs",
    tags=["Audit"]
)
async def get_audit_logs(
    event_type: Optional[str] = Query(None),
    user_id: Optional[str] = Query(None),
    account_id: Optional[str] = Query(None),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500),
    authorization: Optional[str] = Header(None)
):
    """
    Get audit logs (admin endpoint).
    Filters can be applied for analysis.
    """
    # In real scenario, would verify admin role
    user_oid = extract_user_oid(authorization)
    if not user_oid:
        raise HTTPException(status_code=401, detail="Unauthorized")

    logs = orchestrator.audit_logger.get_logs(
        event_type=event_type,
        user_id=user_id,
        account_id=account_id,
        start_date=start_date,
        end_date=end_date,
        limit=limit
    )

    return {
        "logs": [log.model_dump() for log in logs],
        "total": len(logs),
        "filters": {
            "event_type": event_type,
            "user_id": user_id,
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date
        }
    }


@app.get(
    "/api/v1/audit-logs/statistics",
    tags=["Audit"]
)
async def get_audit_statistics(
    authorization: Optional[str] = Header(None)
):
    """Get audit log statistics"""
    user_oid = extract_user_oid(authorization)
    if not user_oid:
        raise HTTPException(status_code=401, detail="Unauthorized")

    stats = orchestrator.audit_logger.get_statistics()
    return stats


# ============================================================================
# Test/Debug Endpoints
# ============================================================================

@app.get(
    "/debug/users",
    tags=["Debug"]
)
async def debug_list_users():
    """
    [DEBUG] List available users for testing.
    Format: Bearer <oid> in Authorization header
    """
    import json
    from pathlib import Path

    users_file = Path("data/users.json")
    if users_file.exists():
        with open(users_file) as f:
            users = json.load(f)
        return {
            "users": [
                {
                    "oid": u["oid"],
                    "name": u["name"],
                    "groups": u["groups"]
                }
                for u in users
            ],
            "usage": "Use 'Bearer <oid>' in Authorization header"
        }
    return {"error": "Users file not found"}


@app.get(
    "/debug/accounts",
    tags=["Debug"]
)
async def debug_list_accounts():
    """[DEBUG] List available accounts"""
    import json
    from pathlib import Path

    accounts_file = Path("data/accounts.json")
    if accounts_file.exists():
        with open(accounts_file) as f:
            accounts = json.load(f)
        return {
            "accounts": [
                {
                    "id": a["id"],
                    "name": a["name"],
                    "industry": a["industry"],
                    "status": a["status"]
                }
                for a in accounts
            ]
        }
    return {"error": "Accounts file not found"}


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status": exc.status_code,
            "correlation_id": request.state.correlation_id if hasattr(request.state, 'correlation_id') else None
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
