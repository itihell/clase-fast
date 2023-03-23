from fastapi import FastAPI
from database.database import Base, engine
from modules.auth import ruters


def create_table():
    Base.metadata.create_all(bind=engine)


create_table()

app = FastAPI()
app.include_router(ruters.router)
