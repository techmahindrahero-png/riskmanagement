"""Asset Schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.asset import AssetType, AssetStatus

class AssetCreate(BaseModel):
    """Create asset schema"""
    name: str
    asset_type: AssetType
    description: Optional[str] = None
    owner: Optional[str] = None
    criticality: Optional[str] = None
    status: AssetStatus = AssetStatus.ACTIVE
    location: Optional[str] = None
    ip_address: Optional[str] = None

class AssetUpdate(BaseModel):
    """Update asset schema"""
    name: Optional[str] = None
    asset_type: Optional[AssetType] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    criticality: Optional[str] = None
    status: Optional[AssetStatus] = None
    location: Optional[str] = None
    ip_address: Optional[str] = None

class AssetResponse(BaseModel):
    """Asset response schema"""
    id: int
    name: str
    asset_type: AssetType
    description: Optional[str]
    owner: Optional[str]
    criticality: Optional[str]
    status: AssetStatus
    location: Optional[str]
    ip_address: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True