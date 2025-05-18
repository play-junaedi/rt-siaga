from pydantic import BaseModel
from datetime import datetime

class PasswordResetTokenBase(BaseModel):
    user_id: str
    token: str
    expires_at: datetime
    used: bool


class PasswordResetTokenCreate(BaseModel):
    user_id: str
    token: str


class PasswordResetTokenResponse(PasswordResetTokenBase):
    id: str

    class Config:
        from_attributes = True