from sqlalchemy.orm import Session
from app.models.announcement import Announcement

def create_announcement(db: Session, data):
    db_announce = Announcement(**data.model_dump())
    db.add(db_announce)
    db.commit()
    db.refresh(db_announce)
    return db_announce

def publish_announcement(db: Session, announce_id: str):
    announce = db.query(Announcement).filter(Announcement.id == announce_id).first()
    if announce:
        announce.is_published = True
        db.commit()
        db.refresh(announce)
    return announce

def get_announcements(db: Session):
    return db.query(Announcement).all()