from sqlite3 import Timestamp
from database.models import DbPost
from routers.schemas import PostBase
from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
import datetime 

def create(db:Session,request:PostBase):
    new_post=DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_post(db: Session):
    return db.query(DbPost).all()

def delete_post(id:int,db:Session):
    post=db.query(DbPost).filter(DbPost.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post  with id {id} not Found')
    # post.update(request.dict())
    db.delete(post)
    db.commit()
    return 'Deleted Sucessufly'
