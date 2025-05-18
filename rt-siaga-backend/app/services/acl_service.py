from sqlalchemy.orm import Session
from app.models.user_role import UserRole
from app.models.role import Role

def assign_role(db: Session, user_id: str, role_id: str, by_admin_id: str):
    db_user_role = UserRole(
        user_id=user_id,
        role_id=role_id
    )
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role