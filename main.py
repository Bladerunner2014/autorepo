from schemas import schemas
from dotenv import dotenv_values
from fastapi import FastAPI, Header
import logging
# from log import log
from fastapi.middleware.cors import CORSMiddleware
from manager.manager import DriverManager, AutoManager, Service

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


# logger = logging.getLogger(__name__)


@app.post("/auto/", response_model=schemas.Auto, tags=["Auto"])
def create_auto(auto: schemas.Auto):
    m = AutoManager()
    res = m.creator(auto)

    return res


@app.get("/auto/", tags=["Auto"])
def read_autos():
    m = AutoManager()
    res = m.all()

    return res


@app.get("/auto/plate", response_model=schemas.Auto, tags=["Auto"])
def read_auto(auto_plate: str = Header(...)):
    m = AutoManager()
    res = m.reader(auto_plate)

    return res


@app.delete("/auto/", tags=["Auto"])
def delete_auto(auto_plate: str):
    m = AutoManager()
    res = m.delete(auto_plate)

    return res


@app.patch("/auto/", tags=["Auto"])
def update_auto(auto_plate, auto: dict):
    m = AutoManager()
    res = m.update(car_plate=auto_plate, new_values=auto)

    return res


@app.post("/driver/", response_model=schemas.Driver, tags=["Driver"])
def create_driver(driver: schemas.Driver):
    m = DriverManager()
    res = m.creator(driver)

    return res


@app.get("/driver/", tags=["Driver"])
def read_drivers():
    m = DriverManager()
    res = m.all()

    return res


@app.get("/driver/phone/", response_model=schemas.Auto, tags=["Driver"])
def read_driver(phone_number: str = Header(...)):
    m = DriverManager()
    res = m.reader(phone_number)

    return res


@app.delete("/driver/", tags=["Driver"])
def delete_driver(phone_number: str):
    m = DriverManager()
    res = m.delete(phone_number)

    return res


@app.patch("/driver/", tags=["Driver"])
def update_driver(phone_number, driver: dict):
    m = DriverManager()
    res = m.update(phone_number=phone_number, new_values=driver)

    return res


"""Services"""


@app.post("/service/", tags=["Service"])
def create_service(service: schemas.Service):
    handler = Service()
    res = handler.creator(service)

    return res


@app.get("/service/", tags=["Service"])
def read_services():
    handler = Service()
    res = handler.all()

    return res


@app.get("/service/service", response_model=schemas.Service, tags=["Service"])
def read_service(service_id: str = Header(...)):
    handler = Service()
    res = handler.reader(service_id)

    return res


@app.delete("/service/", tags=["Service"])
def delete_service(service_id: str):
    handler = Service()
    res = handler.delete(service_id)

    return res


@app.patch("/service/", tags=["Service"])
def update_service(service_id, service: dict):
    handler = Service()
    res = handler.update(service_id=service_id, new_values=service)

    return res

# log.setup_logger()
