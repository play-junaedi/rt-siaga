from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationBase, NotificationResponse
from app.services.notification_service import send_notification, mark_as_read
from app.database import get_db

router = APIRouter(prefix="/notifications", tags=["Notifikasi"])

@router.post("/", response_model=NotificationResponse)
def send(notif: NotificationBase, db: Session = Depends(get_db)):
    return send_notification(db, notif.user_id, notif.title, notif.message, notif.type)

@router.put("/{notif_id}/read")
def read_notif(notif_id: str, db: Session = Depends(get_db)):
    result = mark_as_read(db, notif_id)
    if not result:
        raise HTTPException(status_code=404, detail="Notifikasi tidak ditemukan")
    return {"detail": "Notifikasi ditandai sudah dibaca"}