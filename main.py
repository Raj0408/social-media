
from fastapi import FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from databases import Database

DATABASE_URL = "postgresql://postgres:root@localhost/temp"


database = Database(DATABASE_URL)



try: 
    conn = database.connect(DATABASE_URL)

except Exception as error:

    print("Error",error)

class Posts(BaseModel):
    title :str
    content : str
    rating : Optional[int] = 0

app = FastAPI()


dicts = [{
    "1" : "this is first page",
    "2" : "this is second page", 
}]


@app.get("/")
async def read_root():
    posts = database.execute(""" SELECT * FROM posts""")
    return {"posts" : posts}

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
    # query = f"INSERT INTO posts(title, content, rating) VALUES ({title}),({content}),({rating})) RETURNING id"
    # try:
    #     last_record_id = await database.execute(query=query, values=payload.model_dump())
    # except:
    #     print("Error Occured")
    return {"id": last_record_id, **payload.model_dump()}
    





