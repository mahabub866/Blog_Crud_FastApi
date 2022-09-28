from typing import List
from pydantic import BaseModel
from datetime import datetime
import random
import time
random_id=random.randint(0,999)

class PostBase(BaseModel):
    image_url:str
    title:str
    content:str
    creator:str
 
# inside userdisplay
class PostDisplay(BaseModel):
    id:int
    image_url:str
    title:str
    content:str
    creator:str
    timestamp:datetime
    class Config():
        orm_mode = True


class RandBase(BaseModel):
    rnd:int| None=random_id
    
    
    
class RandDisplay(BaseModel):
    rnd: int
    
    class Config():
        orm_mode = True
    