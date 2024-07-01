
from fastapi import Depends, FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from databases import Database
from sqlalchemy.orm import Session
from . import models
from databases import database as db
from routers import posts , users

DATABASE_URL = "postgresql://postgres:root@localhost/temp"
database = Database(DATABASE_URL)

models.Base.metadata.create_all(bind=db.engine)



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
def sql(db : Session = Depends(db.get_db)):
    posts = db.query(models.Posts).all()
    return {"return " : posts}

app.include_router(posts.router)
# app.include_router(users.router)





