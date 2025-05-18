from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnnouncementBase(BaseModel):
    title: str
    content: str
    attachment_url: Optional[str] = None
    scheduled_time: Optional[datetime] = None


class AnnouncementCreate(AnnouncementBase):
    created_by: str


class AnnouncementResponse(AnnouncementBase):
    id: str
    created_by: str
    created_at: datetime
    is_published: bool

    class Config:
        from_attributes = True