"""
Data models and schemas for RM Intelligence Experience
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


# ============================================================================
# Identity & Access Models
# ============================================================================

class UserContext(BaseModel):
    """User context extracted from OBO token"""
    oid: str = Field(..., description="Object ID from Entra")
    name: str
    email: str
    groups: List[str] = Field(default_factory=list)
    correlationId: str


class AccessCheckResult(BaseModel):
    """Result of ACL check"""
    allowed: bool
    reason: Optional[str] = None


# ============================================================================
# Data Source Models
# ============================================================================

class Account(BaseModel):
    """CRM Account"""
    id: str
    name: str
    industry: str
    ownerGroupId: str
    ownerId: str
    createdAt: str
    lastActivityAt: str
    revenue: Optional[float] = None
    status: str


class Transaction(BaseModel):
    """Transaction record"""
    id: str
    accountId: str
    amount: float
    currency: str
    category: str
    date: str
    description: str
    sourceUri: str


class Email(BaseModel):
    """Email record"""
    id: str
    accountId: str
    frm: str = Field(alias="from")
    to: str
    subject: str
    body: str
    date: str
    sourceUri: str

    class Config:
        populate_by_name = True


class Document(BaseModel):
    """Knowledge document"""
    id: str
    accountId: str
    title: str
    content: str
    category: str
    source: str
    sourceUri: str
    createdAt: str


class SearchIndexDocument(BaseModel):
    """Search index document with ACL"""
    id: str
    accountId: str
    title: str
    content: str
    category: str
    source: str
    sourceUri: str
    aclGroups: List[str] = Field(default_factory=list)
    score: Optional[float] = None


# ============================================================================
# API Request/Response Models
# ============================================================================

class InsightRequest(BaseModel):
    """Request for account insights"""
    question: Optional[str] = None
    detailLevel: str = Field(default="summary", description="summary or detailed")


class Citation(BaseModel):
    """Citation with source reference"""
    text: str
    sourceUri: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    source: str = Field(default="", description="Type: email, transaction, document, etc")


class RiskIndicator(BaseModel):
    """Risk indicator"""
    name: str
    score: float = Field(..., ge=0.0, le=10.0)
    reason: str
    citationIds: List[str] = Field(default_factory=list)


class Opportunity(BaseModel):
    """Growth opportunity"""
    name: str
    score: float = Field(..., ge=0.0, le=10.0)
    reason: str
    citationIds: List[str] = Field(default_factory=list)


class NextStep(BaseModel):
    """Recommended next step"""
    action: str
    owner: Optional[str] = None
    dueDate: Optional[str] = None
    reason: str
    citationIds: List[str] = Field(default_factory=list)


class InsightResponse(BaseModel):
    """Response with insights and citations"""
    accountId: str
    accountName: str
    summary: str
    risks: List[RiskIndicator] = Field(default_factory=list)
    opportunities: List[Opportunity] = Field(default_factory=list)
    nextSteps: List[NextStep] = Field(default_factory=list)
    citations: List[Citation] = Field(default_factory=list)
    generatedAt: str


# ============================================================================
# Audit Log Models
# ============================================================================

class AuditLogEvent(BaseModel):
    """Audit log event"""
    timestamp: str
    eventType: str  # query_answered, access_denied, access_allowed, etc
    userId: str
    correlationId: str
    accountId: Optional[str] = None
    citationIds: List[str] = Field(default_factory=list)
    resultSummary: Optional[str] = None
    status: str  # success, denied, error
    details: Optional[Dict[str, Any]] = None


# ============================================================================
# Internal Processing Models
# ============================================================================

class SearchResult(BaseModel):
    """Search result with relevance score"""
    id: str
    title: str
    content: str
    source: str
    sourceUri: str
    score: float
    aclGroups: List[str] = Field(default_factory=list)


class ContextPackage(BaseModel):
    """Evidence package for LLM"""
    accountId: str
    accountName: str
    transactions: List[Dict[str, Any]] = Field(default_factory=list)
    emails: List[Dict[str, Any]] = Field(default_factory=list)
    documents: List[Dict[str, Any]] = Field(default_factory=list)
    riskScores: Dict[str, float] = Field(default_factory=dict)
    opportunityScores: Dict[str, float] = Field(default_factory=dict)


class LLMRequest(BaseModel):
    """Request to LLM for text generation"""
    accountId: str
    accountName: str
    contextData: str
    riskAnalysis: str
    opportunityAnalysis: str
    instructionText: str


class LLMResponse(BaseModel):
    """Response from LLM"""
    summary: str
    risks: List[Dict[str, Any]] = Field(default_factory=list)
    opportunities: List[Dict[str, Any]] = Field(default_factory=list)
    nextSteps: List[Dict[str, Any]] = Field(default_factory=list)
    usedCitations: List[str] = Field(default_factory=list)
