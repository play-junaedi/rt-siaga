from sqlalchemy.orm import Session
from app.models.role_permission import RolePermission

def grant_permission(db: Session, role_id: str, permission_id: str, admin_id: str):
    db_grant = RolePermission(
        role_id=role_id,
        permission_id=permission_id,
        assigned_by=admin_id
    )
    db.add(db_grant)
    db.commit()
    db.refresh(db_grant)
    return db_grant

def get_role_permissions(db: Session, role_id: str):
    return db.query(RolePermission).filter(RolePermission.role_id == role_id).all()