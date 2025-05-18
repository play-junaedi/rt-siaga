from pydantic import BaseModel
from datetime import datetime

class LoginHistoryBase(BaseModel):
    user_id: str
    ip_address: str
    device_info: str
    success: bool


class LoginHistoryCreate(LoginHistoryBase):
    pass


class LoginHistoryResponse(LoginHistoryBase):
    id: str
    login_time: datetime

    class Config:
        from_attributes = True