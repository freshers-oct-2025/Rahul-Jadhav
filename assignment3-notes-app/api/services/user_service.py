from sqlalchemy.orm import Session
from api.repository.user_repository import UserRepository
from models.user_model import User
from schemas.user_schema import UserCreate

class UserService:

    @staticmethod
    def create_user(db: Session, data: UserCreate):
        existing = UserRepository.get_by_username(db, data.username)
        if existing:
            raise Exception("Username already exists")
        user = User(username=data.username, password=data.password, role=data.role)
        return UserRepository.create(db, user)

    @staticmethod
    def authenticate(db: Session, username: str, password: str):
        user = UserRepository.get_by_username(db, username)
        if not user or user.password != password:
            return None
        return user
    
    @staticmethod
    def get_all_users(db):
        return UserRepository.get_all(db)

    @staticmethod
    def get_user_by_id(db, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        return user
