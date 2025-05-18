from sqlalchemy.orm import Session
from app.models.user_role import UserRole

def assign_role_to_user(db: Session, user_id: str, role_id: str, assigned_by: str):
    db_user_role = UserRole(
        user_id=user_id,
        role_id=role_id
    )
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role

def get_user_roles(db: Session, user_id: str):
    return db.query(UserRole).filter(UserRole.user_id == user_id).all()