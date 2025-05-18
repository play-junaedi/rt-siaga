from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.announcement import Announcement
from app.schemas.announcement import AnnouncementCreate, AnnouncementResponse
from app.services.announcement_service import create_announcement, publish_announcement
from app.database import get_db

router = APIRouter(prefix="/announcements", tags=["Pengumuman"])

@router.post("/", response_model=AnnouncementResponse)
def create_new_announcement(announce: AnnouncementCreate, db: Session = Depends(get_db)):
    return create_announcement(db, announce)

@router.put("/{announce_id}/publish")
def publish(announce_id: str, db: Session = Depends(get_db)):
    result = publish_announcement(db, announce_id)
    if not result:
        raise HTTPException(status_code=404, detail="Pengumuman tidak ditemukan")
    return {"detail": "Pengumuman telah dipublikasikan"}