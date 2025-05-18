from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.database import Base

class SOSAlert(Base):
    __tablename__ = "sos_alerts"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    location_lat = Column(String)
    location_lng = Column(String)
    description = Column(Text, nullable=True)
    triggered_at = Column(DateTime, default=datetime.utcnow)
    resolved = Column(Boolean, default=False)
    resolved_by = Column(String, ForeignKey("users.id"), nullable=True)
    resolved_at = Column(DateTime, nullable=True)