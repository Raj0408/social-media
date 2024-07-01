from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Posts(Base):
    __tablename__ = "socialpost"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    rating = Column(Integer, default=0)


