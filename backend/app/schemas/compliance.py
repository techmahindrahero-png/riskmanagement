"""Compliance Schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.compliance import ComplianceStatus

class ComplianceCreate(BaseModel):
    """Create compliance schema"""
    standard: str
    requirement: str
    description: Optional[str] = None
    status: ComplianceStatus = ComplianceStatus.NOT_STARTED
    owner: Optional[str] = None
    evidence: Optional[str] = None
    gap_analysis: Optional[str] = None
    remediation_plan: Optional[str] = None
    target_date: Optional[datetime] = None

class ComplianceUpdate(BaseModel):
    """Update compliance schema"""
    standard: Optional[str] = None
    requirement: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ComplianceStatus] = None
    owner: Optional[str] = None
    evidence: Optional[str] = None
    gap_analysis: Optional[str] = None
    remediation_plan: Optional[str] = None
    target_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None

class ComplianceResponse(BaseModel):
    """Compliance response schema"""
    id: int
    standard: str
    requirement: str
    description: Optional[str]
    status: ComplianceStatus
    owner: Optional[str]
    evidence: Optional[str]
    gap_analysis: Optional[str]
    remediation_plan: Optional[str]
    target_date: Optional[datetime]
    completion_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True