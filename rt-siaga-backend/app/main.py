from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import sync_engine, Base
from app.core.rbac_middleware import rbac_middleware
from app.core.auth_middleware import auth_middleware
from app.api.v1.routers import (
    auth,
    sos,
    forum,
    cctv,
    chatbot,
    notification,
    acl,
    organization,
)

# Inisialisasi aplikasi
app = FastAPI(title="RT-Siaga API", version="1.0.0")

# Middleware
app.add_middleware(auth_middleware)
app.add_middleware(rbac_middleware)

# Routers
app.include_router(auth.router)
app.include_router(sos.router)
app.include_router(forum.router)
app.include_router(cctv.router)
app.include_router(chatbot.router)
app.include_router(notification.router)
app.include_router(acl.router)
app.include_router(organization.router)

# Buat semua tabel jika belum ada
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=sync_engine)

@app.get("/")
def read_root():
    return {"message": "Selamat datang di RT-Siaga Backend!"}