from fastapi import HTTPException, status
from fastapi.responses import ORJSONResponse
import httpx
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


@app.patch("/auto/")
def update_car(car: schemas.Autoschema):
    db = SessionLocal()
    db_user = auto_dao.update_car(db, car)
    return db_user


@app.post("/assign/")
def assign(car_plate: str, driver_id: str):
    db = SessionLocal()

    plate = auto_dao.get_car_by_plate(db, plate=car_plate)
    if plate is None:
        raise HTTPException(status_code=404, detail="car not found")

    if plate.assigned_to is not None:
        raise HTTPException(status_code=404, detail="car already in use")

    # TODO: UPDATE CAR
    plate.assigned_to = driver_id
    auto_dao.update_car(db, plate)

    # try:
    #     response = httpx.post(config["DRIVER_REPO"], data={'car_plate': car_plate, "driver_id": driver_id})
    # except Exception as error:
    #     logger.error("error in sending request to drivers repo")
    #     logger.error(error)
    #     raise Exception
    # return response.status_code, response.json()
    return ORJSONResponse(status_code=status.HTTP_200_OK, content={"message": "car assigned successfully!"})


log.setup_logger()
