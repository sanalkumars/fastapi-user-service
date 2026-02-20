from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.routes import auth , user

Base.metadata.create_all(bind=engine)  #This will create the tables if they are not existing 

app = FastAPI(title="Production FastAPI Server")

app.include_router(auth.router )
app.include_router( user.router )