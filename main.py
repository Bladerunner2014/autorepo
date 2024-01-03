from fastapi import HTTPException, status
from fastapi.responses import ORJSONResponse

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
def create_car(car: schemas.Autoschema):
    db = SessionLocal()
    db_user = auto_dao.get_car_by_plate(db, car.plate_number)
    if db_user:
        raise HTTPException(status_code=400, detail="Car already registered")
    res = auto_dao.create_car(db=db, car=car)
    return res


@app.get("/auto/")
def read_cars(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    cars = auto_dao.get_cars(db, skip=skip, limit=limit)
    if cars is None:
        raise HTTPException(status_code=404, detail="no car found")
    return cars


@app.get("/car/{car_plate}", response_model=schemas.Autoschema)
def read_car(car_plate):
    db = SessionLocal()
    plate = auto_dao.get_car_by_plate(db, plate=car_plate)
    if plate is None:
        raise HTTPException(status_code=404, detail="car not found")
    return plate


@app.delete("/users/{car_plate}", response_model=schemas.Autoschema)
def delete_car(car_plate: str):
    db = SessionLocal()
    db_user = auto_dao.get_car_by_plate(db, car_plate)
    if not db_user:
        raise HTTPException(status_code=404, detail="car not found")
    plate = auto_dao.delete_car(db, plate=car_plate)
    return ORJSONResponse(status_code=status.HTTP_200_OK, content={"message": "car deleted successfully"})


log.setup_logger()
