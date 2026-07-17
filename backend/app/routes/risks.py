"""Risk Management Routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.risk import Risk, RiskRegister
from app.models.user import User
from app.schemas.risk import RiskCreate, RiskUpdate, RiskResponse, RiskRegisterResponse
from app.auth.security import get_current_user
from app.services.risk_engine import RiskAssessmentEngine

router = APIRouter(prefix="/risks", tags=["risks"])

@router.get("/", response_model=List[RiskResponse])
def list_risks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all risks"""
    risks = db.query(Risk).offset(skip).limit(limit).all()
    return risks

@router.post("/", response_model=RiskResponse)
def create_risk(
    risk_create: RiskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create new risk"""
    risk = RiskAssessmentEngine.create_risk(db, risk_create)
    return risk

@router.get("/{risk_id}", response_model=RiskResponse)
def get_risk(
    risk_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get risk by ID"""
    risk = db.query(Risk).filter(Risk.id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    return risk

@router.put("/{risk_id}", response_model=RiskResponse)
def update_risk(
    risk_id: int,
    risk_update: RiskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update risk"""
    risk = db.query(Risk).filter(Risk.id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    
    risk = RiskAssessmentEngine.update_risk(db, risk, risk_update)
    return risk

@router.delete("/{risk_id}")
def delete_risk(
    risk_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete risk"""
    risk = db.query(Risk).filter(Risk.id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    
    db.delete(risk)
    db.commit()
    return {"message": "Risk deleted successfully"}

@router.get("/register/overview", response_model=RiskRegisterResponse)
def get_risk_register_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get risk register overview"""
    risk_register = db.query(RiskRegister).first()
    if not risk_register:
        risk_register = RiskRegister(name="Organization Risk Register")
        db.add(risk_register)
        db.commit()
    
    RiskAssessmentEngine.update_risk_register_stats(db, risk_register)
    db.refresh(risk_register)
    return risk_register