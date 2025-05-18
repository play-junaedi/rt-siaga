from sqlalchemy.orm import Session
from app.models.cctv_source import CCTVSource

def add_cctv_source(db: Session, source_data):
    db_source = CCTVSource(**source_data.model_dump())
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source

def get_cctv_sources(db: Session):
    return db.query(CCTVSource).all()