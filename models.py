from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import database as db

class Posts(db.Base):
    __tablename__ = "socialpost"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    rating = Column(Integer, default=0)


class User(db.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    posts = relationship("Posts", back_populates="owner")