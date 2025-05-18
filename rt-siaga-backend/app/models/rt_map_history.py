from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class RTMapHistory(Base):
    __tablename__ = "rt_map_history"

    id = Column(String, primary_key=True)
    profile_id = Column(String, ForeignKey("rt_profiles.id"))
    old_geojson = Column(Text, nullable=True)
    new_geojson = Column(Text, nullable=False)
    updated_by = Column(String, ForeignKey("users.id"))
    update_time = Column(DateTime, default=datetime.utcnow)
    reason = Column(Text, nullable=True)