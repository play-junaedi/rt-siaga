from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class ModerationHistory(Base):
    __tablename__ = "moderation_history"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))          # Moderator
    action_type = Column(String, nullable=False)              # 'delete_answer', 'mark_best', dll.
    target_type = Column(String, nullable=False)              # 'question', 'answer'
    target_id = Column(String, nullable=False)                # ID question/answer
    reason = Column(Text, nullable=True)                     # Alasan aksi
    timestamp = Column(DateTime, default=datetime.utcnow)