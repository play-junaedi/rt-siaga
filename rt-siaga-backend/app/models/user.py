from sqlalchemy import Column, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    password_hash = Column(String)
    role = Column(Enum('warga', 'rt', 'rw', 'admin', name='user_roles'))
    status = Column(Enum('aktif', 'nonaktif', 'pending', name='user_status'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = relationship("UserRole", back_populates="user")

    # Relasi (opsional, bisa tambahkan jika pakai relationship)