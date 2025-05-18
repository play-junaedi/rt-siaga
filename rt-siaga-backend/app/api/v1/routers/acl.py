from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate, RoleResponse
from app.schemas.permission import PermissionCreate, PermissionResponse
from app.schemas.user_role import UserRoleCreate
from app.services.acl_service import assign_role_to_user, create_role, create_permission
from app.database import get_db

router = APIRouter(prefix="/acl", tags=["Access Control List"])

@router.post("/roles", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.post("/assign-role", response_model=UserRoleCreate)
def assign_role(data: UserRoleCreate, db: Session = Depends(get_db)):
    return assign_role_to_user(db, data.user_id, data.role_id)