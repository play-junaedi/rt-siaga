from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SOSAlertBase(BaseModel):
    user_id: str
    location_lat: str
    location_lng: str
    description: Optional[str] = None


class SOSAlertCreate(SOSAlertBase):
    pass


class SOSAlertResponse(SOSAlertBase):
    id: str
    triggered_at: datetime
    resolved: bool
    resolved_by: Optional[str] = None
    resolved_at: Optional[datetime] = None

    class Config:
        from_attributes = True