from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey, Text, Column
from sqlalchemy.orm import relationship
from app.database import Base

class Audit(Base):
    __tablename__ = "audits"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    audit_type = Column(String(100), default="internal")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(50), default="planned")
    scope = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    findings = relationship("Finding", back_populates="audit")

class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True, index=True)
    audit_id = Column(Integer, ForeignKey("audits.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    severity = Column(String(50), default="medium")
    status = Column(String(50), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    audit = relationship("Audit", back_populates="findings")
    corrective_actions = relationship("CorrectiveAction", back_populates="finding")

class CorrectiveAction(Base):
    __tablename__ = "corrective_actions"
    id = Column(Integer, primary_key=True, index=True)
    finding_id = Column(Integer, ForeignKey("findings.id"), nullable=False)
    action_description = Column(Text)
    due_date = Column(DateTime)
    status = Column(String(50), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    finding = relationship("Finding", back_populates="corrective_actions")
