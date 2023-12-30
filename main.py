from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from db.orm_database import SessionLocal, engine
from dotenv import dotenv_values
from fastapi import FastAPI
import logging
from log import log
from fastapi.middleware.cors import CORSMiddleware
from dao import auto_dao


models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#
# tags_metadata = [
#     {
#         "name": "form_auto_dao",
#         "description": "With this endpoint you can POST/PUT/GET/DELETE documents in mongoDB.",
#     },
#     {
#         "name": "auth",
#         "description": "This endpoint handle the authentication of users.",
#
#     },
#     {
#         "name": "form_struct_auto_dao",
#         "description": "To auto_dao forms structs in database (only admin can access these endpoints).",
#
#     }
# ]
app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
config = dotenv_values(".env")
logger = logging.getLogger(__name__)


@app.post("/auto/", response_model=schemas.Autoschema)
def create_user(car: schemas.Autoschema, db: Session = Depends(get_db)):
    db_user = auto_dao.get_car_by_plate(db, plate=car.plate_number)
    if db_user:
        raise HTTPException(status_code=400, detail="Car already registered")
    return auto_dao.create_car(db=db, car=car)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = auto_dao.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = auto_dao.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return auto_dao.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = auto_dao.get_items(db, skip=skip, limit=limit)
#     return items
#
#
# log.setup_logger()
