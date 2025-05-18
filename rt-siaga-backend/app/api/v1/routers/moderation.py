from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.moderation import ModerationCreate
from app.services.moderation_service import delete_answer, mark_answer_as_best, report_answer, delete_question
from app.database import get_db

router = APIRouter(prefix="/moderation", tags=["Moderasi Forum"])

@router.delete("/questions/{question_id}")
def moderate_delete_question(
    question_id: str,
    moderator_id: str,
    db: Session = Depends(get_db)
):
    result = delete_question(db, question_id, moderator_id)
    if not result:
        raise HTTPException(status_code=404, detail="Pertanyaan tidak ditemukan")
    return {"detail": "Pertanyaan berhasil dihapus"}

@router.delete("/answers/{answer_id}")
def moderate_delete_answer(
    answer_id: str,
    moderator_id: str,
    reason: str = None,
    db: Session = Depends(get_db)
):
    result = delete_answer(db, answer_id, moderator_id, reason)
    if not result:
        raise HTTPException(status_code=404, detail="Jawaban tidak ditemukan")
    return {"detail": "Jawaban dihapus dari sistem"}