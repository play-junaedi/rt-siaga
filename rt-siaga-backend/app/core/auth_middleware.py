# auth_middleware.py

from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import get_current_user
from sqlalchemy.orm import Session
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def auth_middleware(request: Request, call_next):
    excluded_paths = ["/docs", "/openapi.json", "/auth/login"]

    if request.url.path in excluded_paths:
        return await call_next(request)

    try:
        db: Session = next(get_db())
        token = await oauth2_scheme(request)
        user = get_current_user(db, token)
        request.state.user = user
    except Exception as e:
        return HTTPException(status_code=401, detail="Autentikasi gagal")

    return await call_next(request)