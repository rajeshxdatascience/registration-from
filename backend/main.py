from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from pydantic import BaseModel
import models

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

Base.metadata.create_all(bind=engine)

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "User created successfully",
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not create user")
