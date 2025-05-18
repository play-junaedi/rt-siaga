from sqlalchemy.orm import Session
from app.models.chat_history import ChatHistory

def send_query(db: Session, user_id: str, query: str):
    response = generate_response(query)

    db_chat = ChatHistory(
        id=f"chat_{datetime.utcnow().timestamp()}",
        user_id=user_id,
        query_text=query,
        response_text=response
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def generate_response(query: str):
    if "surat" in query.lower():
        return "Silakan datang ke balai RT dengan membawa fotokopi KTP dan KK."
    elif "posyandu" in query.lower():
        return "Posyandu buka setiap Rabu jam 08:00 - 12:00 di balai RT."
    else:
        return "Maaf, saya belum bisa menjawab pertanyaan tersebut."

def get_chat_history(db: Session, user_id: str):
    return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).all()