from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.organization_position import OrganizationPosition
from app.schemas.organization import OrganizationPositionCreate, OrganizationPositionResponse
from app.services.organization_service import update_organization_position
from app.database import get_db

router = APIRouter(prefix="/organization", tags=["Struktur Organisasi"])

@router.put("/{position_id}")
def update_position(position_id: str, new_user_id: str, db: Session = Depends(get_db)):
    result = update_organization_position(db, position_id, new_user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Posisi tidak ditemukan")
    return {"detail": "Jabatan berhasil diperbarui"}