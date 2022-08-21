
from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship


class DbPost(Base):
    __tablename__='post'
    id=Column(Integer,primary_key=True,index=True)
    image_url=Column(String)
    title=Column(String)
    content=Column(String)
    creator=Column(String)
    timestamp=Column(DateTime)
    # user_id=Column(Integer,ForeignKey('users.id'))
    # items= relationship("DbArticle", back_populates="user")

