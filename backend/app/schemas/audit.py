"""Audit Schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.audit import AuditStatus, FindingSeverity, FindingStatus

class AuditCreate(BaseModel):
    """Create audit schema"""
    title: str
    description: Optional[str] = None
    audit_type: Optional[str] = None
    status: AuditStatus = AuditStatus.PLANNED
    scope: Optional[str] = None
    auditor: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class AuditUpdate(BaseModel):
    """Update audit schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    audit_type: Optional[str] = None
    status: Optional[AuditStatus] = None
    scope: Optional[str] = None
    auditor: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class AuditResponse(BaseModel):
    """Audit response schema"""
    id: int
    title: str
    description: Optional[str]
    audit_type: Optional[str]
    status: AuditStatus
    scope: Optional[str]
    auditor: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    total_findings: int
    critical_findings: int
    high_findings: int
    medium_findings: int
    low_findings: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class AuditFindingCreate(BaseModel):
    """Create audit finding schema"""
    audit_id: int
    title: str
    description: str
    severity: FindingSeverity
    status: FindingStatus = FindingStatus.OPEN
    area: Optional[str] = None
    recommendation: Optional[str] = None
    corrective_action: Optional[str] = None
    responsible_party: Optional[str] = None
    target_remediation_date: Optional[datetime] = None

class AuditFindingResponse(BaseModel):
    """Audit finding response schema"""
    id: int
    audit_id: int
    finding_id: str
    title: str
    description: str
    severity: FindingSeverity
    status: FindingStatus
    area: Optional[str]
    recommendation: Optional[str]
    corrective_action: Optional[str]
    responsible_party: Optional[str]
    target_remediation_date: Optional[datetime]
    actual_remediation_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True