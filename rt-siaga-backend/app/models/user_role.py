from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    role_id = Column(String, ForeignKey("roles.id"))
    assigned_at = Column(DateTime, default=datetime.utcnow)