from pydantic import BaseModel
from datetime import datetime

class UserRoleBase(BaseModel):
    user_id: str
    role_id: str

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleResponse(UserRoleBase):
    id: str
    assigned_at: datetime

    class Config:
        from_attributes = True