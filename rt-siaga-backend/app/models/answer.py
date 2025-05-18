from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(String, primary_key=True)
    question_id = Column(String, ForeignKey("questions.id"))
    user_id = Column(String, ForeignKey("users.id"))
    answer_text = Column(Text, nullable=False)
    is_best_answer = Column(Boolean, default=False)
    posted_at = Column(DateTime, default=datetime.utcnow)