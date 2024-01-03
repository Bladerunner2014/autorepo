from schemas import schemas
from models.models import Auto


def get_car_by_plate(db, plate: str):
    one_car = db.query(Auto).filter(Auto.plate_number == plate).first()
    db.close()

    return one_car


def get_cars(db, skip: int = 0, limit: int = 100):
    cars = db.query(Auto).offset(skip).limit(limit).all()
    db.close()

    return cars


def delete_car(db, plate: str):
    item = db.query(Auto).filter(Auto.plate_number == plate).first()
    db.delete(item)
    db.commit()
    db.close()
    return "item"


def create_car(db, car: schemas.Autoschema):
    car_itam = Auto(auto_name=car.auto_name, plate_number=car.plate_number, sim_number=car.sim_number,
                    car_model=car.car_model, disabled=car.disabled, connection_status=car.connection_status)
    db.add(car_itam)
    db.commit()
    db.refresh(car_itam)
    db.close()
    return car_itam

# TODO UPDATE CAR
