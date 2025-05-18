# RT-Siaga Backend – FastAPI + PostgreSQL

Backend untuk aplikasi komunitas RT-Siaga menggunakan:
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Alembic Migration
- JWT Auth
- RBAC & ACL

## 🔧 Instalasi

```bash
pip install -r requirements.txt
```

## 🗃️  Migrasi Database
```bash
alembic upgrade head
```

## 🚀 Jalankan Aplikasi
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🐳 Deployment via Docker
```bash
docker-compose up -d
```

## ✅ Fitur Utama
- SOS Alert
- Forum Q&A Moderation
- CCTV Streaming
- AI Chatbot
- Announcement Management
- Access Control List (ACL)
- Organization Management
- Login History & Reset Password
     

 
