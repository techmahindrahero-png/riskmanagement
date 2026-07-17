from datetime import datetime
from sqlalchemy import DateTime, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    policy_type = Column(String(100), default="security")
    status = Column(String(50), default="draft")
    version = Column(String(50), default="1.0.0")
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by_user = relationship("User", back_populates="policies")
    controls = relationship("Control", back_populates="policy")

class Standard(Base):
    __tablename__ = "standards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    framework = Column(String(100))
    version = Column(String(50))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    controls = relationship("Control", back_populates="standard")

class Control(Base):
    __tablename__ = "controls"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    control_type = Column(String(50), default="preventive")
    policy_id = Column(Integer, ForeignKey("policies.id"))
    standard_id = Column(Integer, ForeignKey("standards.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    policy = relationship("Policy", back_populates="controls")
    standard = relationship("Standard", back_populates="controls")

from sqlalchemy import Column
