from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from api.services.user_service import UserService
from core.database import get_db

def get_current_user(username: str = Header(...),password: str = Header(...), db: Session = Depends(get_db)):
    user = UserService.authenticate(db,username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user

def admin_required(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only endpoint")
    return current_user
