from schemas import schemas
from models.models import Auto
from fastapi import HTTPException
from sqlalchemy import inspect


def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs
    }


def get_car_by_plate(db, plate: str) -> Auto:
    one_car: Auto() = db.query(Auto).filter(Auto.plate_number == plate).first()

    db.close()
    return one_car


def get_cars(db, skip: int = 0, limit: int = 100):
    cars = db.query(Auto).offset(skip).limit(limit).all()
    db.close()

    return cars


def delete_car(db, plate: str):
    item: Auto = db.query(Auto).filter(Auto.plate_number == plate).first()
    if item.assigned_to is not None:
        raise HTTPException(status_code=404, detail="car already is in use!")

    db.delete(item)
    db.commit()
    db.close()

    return item


def create_car(db, car: schemas.Autoschema):
    car_itam = Auto(**car.dict())
    db.add(car_itam)
    db.commit()
    db.refresh(car_itam)
    db.close()

    return car_itam


# TODO UPDATE CAR
def update_car(db, car: Auto):
    delete_car(db, car.plate_number)
    car = object_as_dict(car)
    car_itam = Auto(**car)
    db.add(car_itam)
    db.commit()
    db.refresh(car_itam)
    db.close()
    return
