from fastapi import FastAPI
from core.database import Base, engine

from api.routers.user_router import router as user_router
from api.routers.note_router import router as note_router

app = FastAPI(title="Notes App")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(note_router)
