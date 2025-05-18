from sqlalchemy.orm import Session
from app.models.question import Question

def create_question(db: Session, question_data):
    db_question = Question(**question_data.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session):
    return db.query(Question).all()

def delete_question(db: Session, question_id: str):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
    return {"status": "success"}