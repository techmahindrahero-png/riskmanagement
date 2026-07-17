"""Audit Management Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.audit import Audit, AuditFinding
from app.models.user import User
from app.schemas.audit import (
    AuditCreate, AuditUpdate, AuditResponse,
    AuditFindingCreate, AuditFindingResponse
)
from app.auth.security import get_current_user

router = APIRouter(prefix="/audits", tags=["audits"])

@router.get("/", response_model=List[AuditResponse])
def list_audits(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List audits"""
    audits = db.query(Audit).offset(skip).limit(limit).all()
    return audits

@router.post("/", response_model=AuditResponse)
def create_audit(
    audit_create: AuditCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create audit"""
    audit = Audit(**audit_create.dict())
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

@router.get("/{audit_id}", response_model=AuditResponse)
def get_audit(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get audit"""
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    return audit

@router.put("/{audit_id}", response_model=AuditResponse)
def update_audit(
    audit_id: int,
    audit_update: AuditUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update audit"""
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    
    update_data = audit_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(audit, field, value)
    
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

@router.delete("/{audit_id}")
def delete_audit(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete audit"""
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    
    db.delete(audit)
    db.commit()
    return {"message": "Audit deleted successfully"}

@router.post("/{audit_id}/findings", response_model=AuditFindingResponse)
def create_audit_finding(
    audit_id: int,
    finding_create: AuditFindingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create audit finding"""
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    
    finding = AuditFinding(**finding_create.dict())
    finding.audit_id = audit_id
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding

@router.get("/{audit_id}/findings", response_model=List[AuditFindingResponse])
def list_audit_findings(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List audit findings"""
    findings = db.query(AuditFinding).filter(AuditFinding.audit_id == audit_id).all()
    return findings

@router.put("/findings/{finding_id}", response_model=AuditFindingResponse)
def update_audit_finding(
    finding_id: int,
    finding_update: AuditFindingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update audit finding"""
    finding = db.query(AuditFinding).filter(AuditFinding.id == finding_id).first()
    if not finding:
        raise HTTPException(status_code=404, detail="Finding not found")
    
    update_data = finding_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(finding, field, value)
    
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding