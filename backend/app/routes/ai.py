"""AI Services Routes"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.models.user import User
from app.auth.security import get_current_user
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["ai"])

ai_service = AIService()

class RiskAnalysisRequest(BaseModel):
    """Risk analysis request"""
    title: str
    description: str
    likelihood: float
    impact: float

class ComplianceGapRequest(BaseModel):
    """Compliance gap identification request"""
    standard: str
    current_controls: str

class PolicyRecommendationRequest(BaseModel):
    """Policy recommendation request"""
    area: str
    current_policy: Optional[str] = None

class AuditRecommendationRequest(BaseModel):
    """Audit recommendation request"""
    audit_findings: str

@router.post("/analyze-risk")
def analyze_risk(
    request: RiskAnalysisRequest,
    current_user: User = Depends(get_current_user)
):
    """Get AI-assisted risk analysis"""
    result = ai_service.analyze_risk(
        request.title,
        request.description,
        request.likelihood,
        request.impact
    )
    return result

@router.post("/compliance-gaps")
def identify_compliance_gaps(
    request: ComplianceGapRequest,
    current_user: User = Depends(get_current_user)
):
    """Identify compliance gaps"""
    result = ai_service.identify_compliance_gaps(
        request.standard,
        request.current_controls
    )
    return result

@router.post("/policy-recommendation")
def get_policy_recommendation(
    request: PolicyRecommendationRequest,
    current_user: User = Depends(get_current_user)
):
    """Get policy recommendations"""
    result = ai_service.generate_policy_recommendation(
        request.area,
        request.current_policy
    )
    return result

@router.post("/audit-recommendation")
def get_audit_recommendation(
    request: AuditRecommendationRequest,
    current_user: User = Depends(get_current_user)
):
    """Get audit recommendations"""
    result = ai_service.generate_audit_recommendation(
        request.audit_findings
    )
    return result

@router.get("/health")
def check_ai_health(current_user: User = Depends(get_current_user)):
    """Check AI service health"""
    is_healthy = ai_service.health_check()
    return {
        "service": "ollama",
        "model": ai_service.model,
        "healthy": is_healthy,
        "url": ai_service.ollama_url
    }