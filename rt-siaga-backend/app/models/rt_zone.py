from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class RTZone(Base):
    __tablename__ = "rt_zones"

    id = Column(String, primary_key=True)
    profile_id = Column(String, ForeignKey("rt_profiles.id"))
    zone_name = Column(String, nullable=False)
    geojson_boundary = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)