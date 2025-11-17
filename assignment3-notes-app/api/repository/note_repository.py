from sqlalchemy.orm import Session
from models.note_model import Note

class NoteRepository:

    @staticmethod
    def create(db: Session, note: Note):
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def get_all(db: Session):
        return db.query(Note).all()

    @staticmethod
    def get_by_id(db: Session, note_id: int):
        return db.query(Note).filter(Note.id == note_id).first()

    @staticmethod
    def get_by_owner(db: Session, owner_id: int):
        return db.query(Note).filter(Note.owner_id == owner_id).all()

    @staticmethod
    def delete(db: Session, note: Note):
        db.delete(note)
        db.commit()
