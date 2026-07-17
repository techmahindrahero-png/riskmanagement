"""Policy and Standard Schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.policy import PolicyStatus, StandardType

class PolicyCreate(BaseModel):
    """Create policy schema"""
    title: str
    description: Optional[str] = None
    content: str
    status: PolicyStatus = PolicyStatus.DRAFT
    version: str = "1.0"
    owner: Optional[str] = None
    effective_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None

class PolicyUpdate(BaseModel):
    """Update policy schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    status: Optional[PolicyStatus] = None
    version: Optional[str] = None
    owner: Optional[str] = None
    effective_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None

class PolicyResponse(BaseModel):
    """Policy response schema"""
    id: int
    title: str
    description: Optional[str]
    content: str
    status: PolicyStatus
    version: str
    owner: Optional[str]
    effective_date: Optional[datetime]
    expiry_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class StandardCreate(BaseModel):
    """Create standard schema"""
    name: str
    standard_type: StandardType
    description: Optional[str] = None
    version: Optional[str] = None
    requirements_count: int = 0

class StandardResponse(BaseModel):
    """Standard response schema"""
    id: int
    name: str
    standard_type: StandardType
    description: Optional[str]
    version: Optional[str]
    requirements_count: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True