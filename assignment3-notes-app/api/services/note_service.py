from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. repository.note_repository import NoteRepository
from models.note_model import Note
from schemas.note_schema import NoteCreate

class NoteService:

    @staticmethod
    def create_note(db: Session, owner_id: int, data: NoteCreate,current_user_id: int):
        note = Note(title=data.title, content=data.content, owner_id=owner_id,created_by=current_user_id,  updated_by=current_user_id )

        return NoteRepository.create(db, note)

    @staticmethod
    def get_all_notes(db: Session):
        return NoteRepository.get_all(db)

    @staticmethod
    def get_note(db: Session, note_id: int):
        note = NoteRepository.get_by_id(db, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    @staticmethod
    def get_user_notes(db: Session, owner_id: int):
        return NoteRepository.get_by_owner(db, owner_id)

    @staticmethod
    def update_note(db: Session, note_id: int, owner_id: int, data: NoteCreate, user_role: str):
        note = NoteService.get_note(db, note_id)
    
        if user_role != "admin" and note.owner_id != owner_id:
            raise HTTPException(status_code=403, detail="Not allowed to update this note")
        note.title = data.title
        note.content = data.content
        note.updated_by = owner_id
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def delete_note(db: Session, note_id: int, owner_id: int, user_role: str):
        note = NoteService.get_note(db, note_id)
        if user_role != "admin" and note.owner_id != owner_id:
            raise HTTPException(status_code=403, detail="Not allowed to delete this note")
        NoteRepository.delete(db, note)
        return {"message": "Note deleted"}


