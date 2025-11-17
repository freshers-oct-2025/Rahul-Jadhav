from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from .. services.note_service import NoteService
from schemas.note_schema import NoteCreate, NoteResponse
from auth.authentication import get_current_user, admin_required

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return NoteService.create_note(db, current_user.id, note,current_user.id)

@router.get("/", response_model=list[NoteResponse])
def get_my_notes(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return NoteService.get_user_notes(db, current_user.id)

@router.get("/all", response_model=list[NoteResponse])
def get_all_notes(db: Session = Depends(get_db), _ = Depends(admin_required)):
    return NoteService.get_all_notes(db)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    note = NoteService.get_note(db, note_id)
    
    if note.owner_id != current_user.id and current_user.role != "admin":
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Not allowed to view this note")
    return note

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, payload: NoteCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return NoteService.update_note(db, note_id, current_user.id, payload, current_user.role)

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return NoteService.delete_note(db, note_id, current_user.id, current_user.role)


