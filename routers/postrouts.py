from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas import posts
from models import postmodel

router = APIRouter()

@router.post("/creatpost",response_model=posts.post)
async def create_post(payload : posts.postcreate , db : Session = Depends(get_db)):
    new_post = postmodel.Posts(**payload.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/posts",response_model=List[posts.post])
async def get_post(db: Session = Depends(get_db)):
    users = db.query(postmodel.Posts).all()
    print(type(users))
    return users