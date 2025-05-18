from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class RoleEnum(str, Enum):
    warga = "warga"
    rt = "rt"
    rw = "rw"
    admin = "admin"

class StatusEnum(str, Enum):
    aktif = "aktif"
    nonaktif = "nonaktif"
    pending = "pending"


class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    role: RoleEnum
    status: StatusEnum


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    username: Optional[str] = None