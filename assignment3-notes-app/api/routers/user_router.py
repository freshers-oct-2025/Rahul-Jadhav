from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from .. services.user_service import UserService
from schemas.user_schema import UserCreate, UserResponse
from auth.authentication import admin_required

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=UserResponse)
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = UserService.authenticate(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user


@router.get("/")
def get_all_users(db: Session = Depends(get_db), admin = Depends(admin_required)):
    return UserService.get_all_users(db)

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db), admin = Depends(admin_required)):
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
