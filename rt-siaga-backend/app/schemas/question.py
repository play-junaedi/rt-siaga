from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QuestionBase(BaseModel):
    user_id: str
    question_text: str
    category: Optional[str] = None


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: str
    posted_at: datetime
    answered: bool

    class Config:
        from_attributes = True