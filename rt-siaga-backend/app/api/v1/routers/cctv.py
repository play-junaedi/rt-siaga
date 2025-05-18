from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.cctv_source import CCTVSource
from app.services.cctv_service import add_cctv_source, get_cctv_sources
from app.database import get_db
from app.models.cctv_source import CCTVSource
from app.schemas.cctv_source import CCTVSourceResponse, CCTVSourceCreate

router = APIRouter(prefix="/cctv", tags=["CCTV Management"])

@router.get("/", response_model=list[CCTVSourceResponse])
def list_sources(db: Session = Depends(get_db)):
    return get_cctv_sources(db)

@router.post("/", response_model=CCTVSourceResponse)
def add_source(source: CCTVSourceCreate, db: Session = Depends(get_db)):
    return add_cctv_source(db, source)