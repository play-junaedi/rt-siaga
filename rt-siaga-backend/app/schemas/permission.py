from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None


class PermissionCreate(PermissionBase):
    pass


class PermissionResponse(PermissionBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True