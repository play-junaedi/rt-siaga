from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnswerBase(BaseModel):
    question_id: str
    user_id: str
    answer_text: str
    is_best_answer: bool = False


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(AnswerBase):
    id: str
    posted_at: datetime

    class Config:
        from_attributes = True