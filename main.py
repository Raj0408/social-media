
from fastapi import Depends, FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from databases import Database
from sqlalchemy.orm import Session

from . import models
from .database.database import SessionLocal, engine

DATABASE_URL = "postgresql://postgres:root@localhost/temp"
database = Database(DATABASE_URL)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Posts(BaseModel):
    title :str
    content : str
    rating : Optional[int] = 0

app = FastAPI()


dicts = [{
    "1" : "this is first page",
    "2" : "this is second page", 
}]

# @app.on_event("startup")
# async def startup():
#     try:
#         await database.connect()
#     except Exception as error:
#         print("Error occurred during database connection:", error)


@app.get("/sql")
def sql(db : Session = Depends(get_db)):
    return {"return " : "2022"}

@app.get("/")
async def read_root():
    query = "SELECT * FROM posts"
    posts = await database.fetch_all(query=query)
    return {"posts" : posts[2]["title"]}

# @app.get("/{idf:str}")
# def get_id(idf):
#     if idf in dicts.keys():
#         return dicts[idf]


@app.post("/creatpost")
async def create_post(payload : Posts):
    print(payload)
    title = payload.title
    content =payload.content
    rating = payload.rating
    query = f"INSERT INTO posts(title, content, rating) VALUES ((:title),(:content),(:rating))"
    try:
        
        last_record_id = await database.execute(query=query, values=payload.model_dump())
    except Exception as error:
        print("Error Occured" , error)
    return {"id": "last_record_id"}
    





