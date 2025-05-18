from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RolePermissionBase(BaseModel):
    role_id: str
    permission_id: str
    assigned_by: str

class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermissionResponse(RolePermissionBase):
    id: str
    assigned_at: datetime

    class Config:
        from_attributes = True