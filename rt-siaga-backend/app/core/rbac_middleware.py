# rbac_middleware.py

from fastapi import Request, HTTPException
from functools import wraps
from app.services.rbac_service import check_user_has_permission

def rbac_middleware(db_session):
    def middleware(app):
        @app.middleware("http")
        async def check_permissions(request: Request, call_next):
            # Mapping path → permission
            path_to_permission = {
                "/v1/forum/questions": "create_forum_question",
                "/v1/forum/answers": "delete_forum_answer",
                "/v1/sos": "resolve_sos_alert",
                "/v1/cctv": "view_cctv",
                "/v1/announcement": "send_announcement",
                "/v1/acl": "manage_roles_and_permissions",
            }

            required_permission = None
            for path, perm in path_to_permission.items():
                if request.url.path.startswith(path):
                    required_permission = perm
                    break

            current_user = request.state.user if hasattr(request.state, "user") else None
            db = db_session()

            if required_permission and current_user:
                try:
                    check_user_has_permission(db, current_user.id, required_permission)
                except PermissionError as e:
                    db.close()
                    raise HTTPException(status_code=403, detail=str(e))

            db.close()
            return await call_next(request)
        return middleware
    return middleware