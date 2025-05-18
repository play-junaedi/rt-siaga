from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.database import Base

class RTProfile(Base):
    __tablename__ = "rt_profiles"

    id = Column(String, primary_key=True)
    rt_number = Column(String(10), unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    map_geojson = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)