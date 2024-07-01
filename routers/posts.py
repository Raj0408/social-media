from fastapi import APIRouter
import schemas , routers , models
from database.database import *
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


@router.post("/creatpost",response_model=schemas.post)
async def create_post(payload : schemas.postcreate , db : Session = Depends(get_db)):
    # print(payload)
    # title = payload.title
    # content =payload.content
    # rating = payload.rating
    # query = f"INSERT INTO posts(title, content, rating) VALUES ((:title),(:content),(:rating))"
    # try:
        
    #     last_record_id = await database.execute(query=query, values=payload.model_dump())
    # except Exception as error:
    #     print("Error Occured" , error)
    # return {"id": "last_record_id"}
    new_post = models.Posts(**payload.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
