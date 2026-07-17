from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey, Float, Text, Column
from sqlalchemy.orm import relationship
from app.database import Base

class Risk(Base):
    __tablename__ = "risks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    risk_category = Column(String(100))
    likelihood = Column(Integer, default=3)
    impact = Column(Integer, default=3)
    calculated_score = Column(Float, default=0.0)
    status = Column(String(50), default="identified")
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_user = relationship("User", back_populates="risks")
    assessments = relationship("RiskAssessment", back_populates="risk")
    mitigations = relationship("Mitigation", back_populates="risk")

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"
    id = Column(Integer, primary_key=True, index=True)
    risk_id = Column(Integer, ForeignKey("risks.id"), nullable=False)
    assessment_date = Column(DateTime, default=datetime.utcnow)
    likelihood = Column(Integer)
    impact = Column(Integer)
    score = Column(Float)
    mitigation_strategy = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    risk = relationship("Risk", back_populates="assessments")

class Mitigation(Base):
    __tablename__ = "mitigations"
    id = Column(Integer, primary_key=True, index=True)
    risk_id = Column(Integer, ForeignKey("risks.id"), nullable=False)
    strategy = Column(Text, nullable=False)
    status = Column(String(50), default="pending")
    progress = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    risk = relationship("Risk", back_populates="mitigations")
