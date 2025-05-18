from sqlalchemy.orm import Session
from app.models.password_reset_token import PasswordResetToken
import secrets
from datetime import timedelta

def generate_reset_token(db: Session, user_id: str):
    token = secrets.token_urlsafe(32)
    db_token = PasswordResetToken(user_id=user_id, token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def verify_reset_token(db: Session, token: str):
    from datetime import datetime
    db_token = db.query(PasswordResetToken).filter(
        PasswordResetToken.token == token,
        PasswordResetToken.expires_at > datetime.utcnow(),
        PasswordResetToken.used == False
    ).first()

    if not db_token:
        raise ValueError("Token tidak valid atau sudah kadaluarsa")
    return db_token