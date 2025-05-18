from sqlalchemy.orm import Session
from app.models.role_permission import RolePermission

def assign_permission_to_role(db: Session, role_id: str, permission_id: str, assigned_by: str):
    db_rp = RolePermission(
        role_id=role_id,
        permission_id=permission_id,
        assigned_by=assigned_by
    )
    db.add(db_rp)
    db.commit()
    db.refresh(db_rp)
    return db_rp

def check_user_has_permission(db: Session, user_id: str, required_permission: str):
    result = db.execute("""
        SELECT p.name 
        FROM user_roles ur
        JOIN role_permissions rp ON ur.role_id = rp.role_id
        JOIN permissions p ON rp.permission_id = p.id
        WHERE ur.user_id = :user_id AND p.name = :permission
        LIMIT 1
    """, {"user_id": user_id, "permission": required_permission})

    row = result.fetchone()
    if not row:
        raise PermissionError(f"Anda tidak memiliki akses untuk '{required_permission}'")
    return True