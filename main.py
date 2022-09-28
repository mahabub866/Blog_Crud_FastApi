from fastapi import FastAPI
from database.database import engine
from database import models
from routers import post,rand
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.include_router(post.router)
app.include_router(rand.router)


models.Base.metadata.create_all(engine)

origins=[
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/images',StaticFiles(directory='images'),name='images')

