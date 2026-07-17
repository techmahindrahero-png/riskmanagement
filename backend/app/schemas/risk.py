"""Risk Schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.risk import RiskStatus, RiskLevel

class RiskCreate(BaseModel):
    """Create risk schema"""
    title: str
    description: str
    category: Optional[str] = None
    likelihood: float
    impact: float
    status: RiskStatus = RiskStatus.IDENTIFIED
    owner: Optional[str] = None
    mitigation_plan: Optional[str] = None

class RiskUpdate(BaseModel):
    """Update risk schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    likelihood: Optional[float] = None
    impact: Optional[float] = None
    status: Optional[RiskStatus] = None
    owner: Optional[str] = None
    mitigation_plan: Optional[str] = None
    residual_risk: Optional[float] = None

class RiskResponse(BaseModel):
    """Risk response schema"""
    id: int
    title: str
    description: str
    category: Optional[str]
    likelihood: float
    impact: float
    risk_score: float
    risk_level: RiskLevel
    status: RiskStatus
    owner: Optional[str]
    mitigation_plan: Optional[str]
    residual_risk: Optional[float]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RiskRegisterResponse(BaseModel):
    """Risk register response schema"""
    id: int
    name: str
    description: Optional[str]
    total_risks: int
    critical_risks: int
    high_risks: int
    medium_risks: int
    low_risks: int
    average_risk_score: float
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True