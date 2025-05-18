from sqlalchemy.orm import Session
from app.models.sos_alert import SOSAlert

def create_sos_alert(db: Session, alert_data):
    db_alert = SOSAlert(**alert_data.model_dump())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def get_sos_alerts(db: Session):
    return db.query(SOSAlert).all()

def resolve_sos_alert(db: Session, sos_id: str, resolver_id: str):
    sos = db.query(SOSAlert).filter(SOSAlert.id == sos_id).first()
    if sos:
        sos.resolved = True
        sos.resolved_by = resolver_id
        sos.resolved_at = datetime.utcnow()
        db.commit()
        db.refresh(sos)
    return sos