from sqlalchemy.orm import Session
from app.models.organization_position import OrganizationPosition

def update_organization_position(db: Session, position_id: str, new_user_id: str):
    position = db.query(OrganizationPosition).filter(OrganizationPosition.id == position_id).first()
    if not position:
        return None
    position.user_id = new_user_id
    db.commit()
    db.refresh(position)
    return position

def list_organization_positions(db: Session):
    return db.query(OrganizationPosition).all()