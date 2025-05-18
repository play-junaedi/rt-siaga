from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))  # Siapa penerima notifikasi
    title = Column(Text, nullable=False)               # Judul notifikasi
    message = Column(Text, nullable=False)             # Isi pesan
    type = Column(String, nullable=False)              # 'sos', 'pengumuman', 'forum'
    read_status = Column(Boolean, default=False)       # Apakah sudah dibaca?
    sent_at = Column(DateTime, default=datetime.utcnow) # Kapan dikirim