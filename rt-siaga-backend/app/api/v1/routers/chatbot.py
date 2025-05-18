from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.chat_history import ChatHistory
from app.schemas.chatbot import ChatMessageCreate, ChatMessageResponse
from app.services.chatbot_service import send_query, generate_response, get_chat_history
from app.database import get_db

router = APIRouter(prefix="/chatbot", tags=["AI Chatbot"])

@router.post("/query", response_model=ChatMessageResponse)
def ask_bot(chat_data: ChatMessageCreate, db: Session = Depends(get_db)):
    return send_query(db, chat_data.user_id, chat_data.query_text)

@router.get("/history/{user_id}", response_model=list[ChatMessageResponse])
def history(user_id: str, db: Session = Depends(get_db)):
    return get_chat_history(db, user_id)