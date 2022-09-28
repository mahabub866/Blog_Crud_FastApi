
from datetime import datetime
from email.policy import default
from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
import sqlalchemy as sa
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

class DbRand(Base):
    __tablename__='rand'
    id=Column(Integer,primary_key=True,index=True)
    rnd=Column(Integer)
    timestamp=Column(DateTime) 

class UserExamp(Base):
    __tablename__ = 'usersex'

    id=sa.Column(sa.Integer,primary_key=True,index=True)
    name=sa.Column(sa.String)
    email=sa.Column(sa.String,unique=True)
    create_date=sa.Column(sa.DateTime,default=datetime.now,index=True)
    last_login=sa.Column(sa.DateTime,default=datetime.now,index=True)
    password=sa.Column(sa.String)

class Release(SqlAlchemyBase):
    pass