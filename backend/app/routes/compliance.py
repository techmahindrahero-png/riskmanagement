"""Compliance Management Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.compliance import Compliance, ComplianceControl
from app.models.user import User
from app.schemas.compliance import ComplianceCreate, ComplianceUpdate, ComplianceResponse
from app.auth.security import get_current_user

router = APIRouter(prefix="/compliance", tags=["compliance"])

@router.get("/", response_model=List[ComplianceResponse])
def list_compliance(
    skip: int = 0,
    limit: int = 100,
    standard: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List compliance requirements"""
    query = db.query(Compliance)
    if standard:
        query = query.filter(Compliance.standard == standard)
    
    compliances = query.offset(skip).limit(limit).all()
    return compliances

@router.post("/", response_model=ComplianceResponse)
def create_compliance(
    compliance_create: ComplianceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create compliance requirement"""
    compliance = Compliance(**compliance_create.dict())
    db.add(compliance)
    db.commit()
    db.refresh(compliance)
    return compliance

@router.get("/{compliance_id}", response_model=ComplianceResponse)
def get_compliance(
    compliance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get compliance requirement"""
    compliance = db.query(Compliance).filter(Compliance.id == compliance_id).first()
    if not compliance:
        raise HTTPException(status_code=404, detail="Compliance requirement not found")
    return compliance

@router.put("/{compliance_id}", response_model=ComplianceResponse)
def update_compliance(
    compliance_id: int,
    compliance_update: ComplianceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update compliance requirement"""
    compliance = db.query(Compliance).filter(Compliance.id == compliance_id).first()
    if not compliance:
        raise HTTPException(status_code=404, detail="Compliance requirement not found")
    
    update_data = compliance_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(compliance, field, value)
    
    db.add(compliance)
    db.commit()
    db.refresh(compliance)
    return compliance

@router.delete("/{compliance_id}")
def delete_compliance(
    compliance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete compliance requirement"""
    compliance = db.query(Compliance).filter(Compliance.id == compliance_id).first()
    if not compliance:
        raise HTTPException(status_code=404, detail="Compliance requirement not found")
    
    db.delete(compliance)
    db.commit()
    return {"message": "Compliance requirement deleted successfully"}

@router.get("/controls/", response_model=List[dict])
def list_compliance_controls(
    standard: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List compliance controls"""
    query = db.query(ComplianceControl)
    if standard:
        query = query.filter(ComplianceControl.standard == standard)
    
    controls = query.all()
    return controls