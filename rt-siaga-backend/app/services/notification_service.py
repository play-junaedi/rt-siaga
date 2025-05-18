from sqlalchemy.orm import Session
from app.models.notification import Notification

def send_notification(db: Session, user_id: str, title: str, message: str, type: str):
    db_notif = Notification(
        user_id=user_id,
        title=title,
        message=message,
        type=type
    )
    db.add(db_notif)
    db.commit()
    db.refresh(db_notif)
    return db_notif

def mark_as_read(db: Session, notif_id: str):
    notif = db.query(Notification).get(notif_id)
    if notif:
        notif.read_status = True
        db.commit()
        db.refresh(notif)
    return notif