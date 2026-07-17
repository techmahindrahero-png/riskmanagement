"""User Schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.user import UserRole

class UserCreate(BaseModel):
    """Create user schema"""
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    role: UserRole = UserRole.VIEWER

class UserUpdate(BaseModel):
    """Update user schema"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    """User response schema"""
    id: int
    username: str
    email: str
    full_name: Optional[str]
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True