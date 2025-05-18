from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RTProfileBase(BaseModel):
    rt_number: str
    name: str
    description: Optional[str] = None
    map_geojson: Optional[str] = None


class RTProfileCreate(RTProfileBase):
    pass


class RTProfileResponse(RTProfileBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True