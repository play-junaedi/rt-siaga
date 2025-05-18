# app/models/cctv_source.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class CCTVSource(Base):
    __tablename__ = "cctv_sources"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)