from fastapi import APIRouter,Depends,UploadFile,File
from routers.schemas import PostBase
from sqlalchemy.orm import Session
from database.database import get_db
import shutil
import string
import random
from repositery.post import create, delete_post, get_all_post
router=APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('/')
def create_post(request:PostBase,db:Session=Depends(get_db)):
    return create(db,request)

@router.get('/all')
def create_post(db:Session=Depends(get_db)):
    return get_all_post(db)

@router.delete('/{id}')
def delete(id:int,db:Session=Depends(get_db)):
   return delete_post(id,db)

@router.post('/image')
def upload_image(image:UploadFile=File(...)):
    letter=string.ascii_letters
    rand_str=''.join(random.choice(letter) for i in range(6))
    new =f'_{rand_str}.'
    filename=new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}