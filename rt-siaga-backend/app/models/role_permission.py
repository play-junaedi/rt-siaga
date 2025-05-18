from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class RolePermission(Base):
    __tablename__ = "role_permissions"

    id = Column(String, primary_key=True)
    role_id = Column(String, ForeignKey("roles.id"))
    permission_id = Column(String, ForeignKey("permissions.id"))
    assigned_by = Column(String, ForeignKey("users.id"))
    assigned_at = Column(DateTime, default=datetime.utcnow)