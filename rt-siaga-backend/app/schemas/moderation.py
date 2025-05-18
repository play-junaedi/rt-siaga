from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class ModerationAction(str, Enum):
    delete_answer = "delete_answer"
    mark_best = "mark_best"
    report_content = "report_content"
    hide_question = "hide_question"


class ModerationCreate(BaseModel):
    user_id: str
    action_type: ModerationAction
    target_type: str  # 'question' atau 'answer'
    target_id: str
    reason: Optional[str] = None


class ModerationResponse(ModerationCreate):
    id: str
    timestamp: datetime

    class Config:
        from_attributes = True