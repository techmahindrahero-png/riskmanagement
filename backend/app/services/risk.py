from sqlalchemy.orm import Session
from app.models.risk import Risk, RiskAssessment

class RiskService:
    def create_risk(self, db: Session, title: str, description: str, risk_category: str, likelihood: int, impact: int, owner_id: int):
        db_risk = Risk(title=title, description=description, risk_category=risk_category, likelihood=likelihood, impact=impact, owner_id=owner_id)
        db_risk.calculated_score = (likelihood * impact) / 25.0 * 100
        db.add(db_risk)
        db.commit()
        db.refresh(db_risk)
        return db_risk

    def get_risks(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Risk).offset(skip).limit(limit).all()

    def get_risk(self, db: Session, risk_id: int):
        return db.query(Risk).filter(Risk.id == risk_id).first()

    def update_risk(self, db: Session, risk_id: int, title: str = None, likelihood: int = None, impact: int = None):
        db_risk = db.query(Risk).filter(Risk.id == risk_id).first()
        if db_risk:
            if title:
                db_risk.title = title
            if likelihood:
                db_risk.likelihood = likelihood
            if impact:
                db_risk.impact = impact
            db_risk.calculated_score = (db_risk.likelihood * db_risk.impact) / 25.0 * 100
            db.commit()
            db.refresh(db_risk)
        return db_risk
