from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey, Text, Column
from sqlalchemy.orm import relationship
from app.database import Base

class ComplianceFramework(Base):
    __tablename__ = "compliance_frameworks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    framework_type = Column(String(100))
    version = Column(String(50))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    requirements = relationship("ComplianceRequirement", back_populates="framework")

class ComplianceRequirement(Base):
    __tablename__ = "compliance_requirements"
    id = Column(Integer, primary_key=True, index=True)
    framework_id = Column(Integer, ForeignKey("compliance_frameworks.id"))
    requirement_id = Column(String(100))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    framework = relationship("ComplianceFramework", back_populates="requirements")

class ComplianceMapping(Base):
    __tablename__ = "compliance_mappings"
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    requirement_id = Column(Integer, ForeignKey("compliance_requirements.id"))
    verified = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class ComplianceGap(Base):
    __tablename__ = "compliance_gaps"
    id = Column(Integer, primary_key=True, index=True)
    framework_id = Column(Integer, ForeignKey("compliance_frameworks.id"))
    gap_description = Column(Text)
    severity = Column(String(50), default="medium")
    status = Column(String(50), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
