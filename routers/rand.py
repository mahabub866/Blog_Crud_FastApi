from fastapi import APIRouter,Depends,UploadFile,status
from routers.schemas import PostBase, RandBase, RandDisplay
from sqlalchemy.orm import Session
from database.database import get_db
import shutil
import string
import random
from repositery.random import create
router=APIRouter(
    prefix='/rand',
    tags=['Random']
    
)

@router.post('/random',status_code=status.HTTP_201_CREATED)
def create_rand(request:RandBase,db:Session=Depends(get_db)):
    return create(db,request)



