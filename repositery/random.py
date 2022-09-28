
from sqlite3 import Timestamp
from database.models import DbPost, DbRand
from routers.schemas import PostBase, RandBase
from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
import datetime 
import time


def create(db:Session,request:RandBase):
    new_rnd=DbRand(
        rnd=request.rnd,
        timestamp=datetime.datetime.now(),
        
        

    )
    db.add(new_rnd)
    db.commit()
    db.refresh(new_rnd)
    return "Sucessufly Created"
   