from sqlalchemy.orm import Session
from app.models.answer import Answer

def create_answer(db: Session, answer_data):
    db_answer = Answer(**answer_data.model_dump())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def mark_as_best_answer(db: Session, answer_id: str):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        answer.is_best_answer = True
        db.commit()
        db.refresh(answer)
    return answer