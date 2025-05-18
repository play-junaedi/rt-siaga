from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class NotificationType(str, Enum):
    sos = "sos"
    pengumuman = "pengumuman"
    forum = "forum"


class NotificationBase(BaseModel):
    user_id: str
    title: str
    message: str
    type: NotificationType


class NotificationCreate(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
    id: str
    read_status: bool
    sent_at: datetime

    class Config:
        from_attributes = True