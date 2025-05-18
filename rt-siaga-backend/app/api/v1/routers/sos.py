from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.sos_alert import SOSAlert
from app.schemas.sos_alert import SOSAlertCreate, SOSAlertResponse
from app.services.sos_service import create_sos_alert, resolve_sos_alert
from app.database import get_db

router = APIRouter(prefix="/sos", tags=["SOS Alert"])

@router.post("/", response_model=SOSAlertResponse)
def trigger_sos(alert: SOSAlertCreate, db: Session = Depends(get_db)):
    return create_sos_alert(db, alert)

@router.put("/{sos_id}/resolve")
def mark_resolved(sos_id: str, resolver_id: str, db: Session = Depends(get_db)):
    result = resolve_sos_alert(db, sos_id, resolver_id)
    if not result:
        raise HTTPException(status_code=404, detail="SOS tidak ditemukan")
    return {"status": "resolved"}