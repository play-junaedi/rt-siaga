from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from datetime import datetime, timedelta
from app.database import Base

class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    token = Column(String, unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(minutes=30))
    used = Column(Boolean, default=False)