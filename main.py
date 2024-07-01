
from fastapi import Depends, FastAPI
from typing import List, Optional
from fastapi.params import Body
from pydantic import BaseModel
from databases import Database
from sqlalchemy.orm import Session
from models import postmodel
import schemas
from database.database import SessionLocal, engine ,get_db
import schemas.posts
from fastapi import APIRouter , FastAPI
from routers import postrouts


postmodel.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(postrouts.router)




    





