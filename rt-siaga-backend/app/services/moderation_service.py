from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.models.question import Question
from app.models.moderation_history import ModerationHistory

def delete_answer(db: Session, answer_id: str, moderator_id: str, reason: str = None):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        db.delete(answer)
        db.commit()

        history = ModerationHistory(
            id=f"mod_{datetime.utcnow().timestamp()}",
            user_id=moderator_id,
            action_type="delete_answer",
            target_type="answer",
            target_id=answer_id,
            reason=reason
        )
        db.add(history)
        db.commit()
        db.refresh(history)
    return answer


def mark_answer_as_best(db: Session, answer_id: str, moderator_id: str):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        answer.is_best_answer = True
        db.commit()
        db.refresh(answer)

        history = ModerationHistory(
            id=f"mod_{datetime.utcnow().timestamp()}",
            user_id=moderator_id,
            action_type="mark_best",
            target_type="answer",
            target_id=answer_id
        )
        db.add(history)
        db.commit()
        db.refresh(history)
    return answer


def report_answer(db: Session, answer_id: str, reporter_id: str, reason: str):
    history = ModerationHistory(
        id=f"mod_{datetime.utcnow().timestamp()}",
        user_id=reporter_id,
        action_type="report_content",
        target_type="answer",
        target_id=answer_id,
        reason=reason
    )
    db.add(history)
    db.commit()
    db.refresh(history)
    return history