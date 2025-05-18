from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.database import Base

class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(String, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    attachment_url = Column(Text, nullable=True)
    scheduled_time = Column(DateTime, nullable=True)
    created_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, default=False)