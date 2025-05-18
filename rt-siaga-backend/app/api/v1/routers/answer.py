from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate, AnswerResponse
from app.services.answer_service import create_answer, mark_as_best_answer
from app.database import get_db

router = APIRouter(prefix="/answers", tags=["Jawaban Forum"])

@router.post("/", response_model=AnswerResponse)
def post_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    return create_answer(db, answer)

@router.put("/{answer_id}/best")
def set_best(answer_id: str, db: Session = Depends(get_db)):
    result = mark_as_best_answer(db, answer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Jawaban tidak ditemukan")
    return {"detail": "Jawaban ditandai sebagai terbaik"}