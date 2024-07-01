from sqlalchemy.orm import Session 
from models import postmodel , usermodel
from schemas import posts, user



def get_posts(db :Session, post_id:int):
    return db.query(postmodel.Posts).filter(postmodel.Posts.id == post_id).first()
