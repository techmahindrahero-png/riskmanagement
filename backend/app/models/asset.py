from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey, Text, Column
from sqlalchemy.orm import relationship
from app.database import Base

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    asset_type = Column(String(100), default="hardware")
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    criticality = Column(String(50), default="medium")
    status = Column(String(50), default="active")
    location = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
