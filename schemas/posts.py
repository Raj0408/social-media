from pydantic import BaseModel
from typing import Optional



class postcreate(BaseModel):
    title :str
    content : str
    rating : Optional[int] = 0

    class config:
        orm_mode = True


class post(BaseModel):
    title:str
    content: str
    

    class config:
        orm_mode = True