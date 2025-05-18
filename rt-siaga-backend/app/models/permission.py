from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    roles = relationship("RolePermission", back_populates="permission")