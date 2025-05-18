from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionResponse
from app.services.forum_service import create_question, get_questions
from app.database import get_db

router = APIRouter(prefix="/forum", tags=["Forum QnA"])

@router.get("/", response_model=list[QuestionResponse])
def list_questions(db: Session = Depends(get_db)):
    return get_questions(db)

@router.post("/", response_model=QuestionResponse)
def post_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question)