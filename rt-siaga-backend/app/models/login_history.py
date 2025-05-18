from sqlalchemy import Column, String, Text, DateTime, Boolean
from datetime import datetime
from app.database import Base

class LoginHistory(Base):
    __tablename__ = "login_history"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    ip_address = Column(String, nullable=False)
    device_info = Column(String, nullable=False)
    success = Column(Boolean, default=False)
    login_time = Column(DateTime, default=datetime.utcnow)