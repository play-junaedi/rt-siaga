from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from app.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    question_text = Column(Text, nullable=False)
    category = Column(String, nullable=True)
    posted_at = Column(DateTime, default=datetime.utcnow)
    answered = Column(Boolean, default=False)