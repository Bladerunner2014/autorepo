from sqlalchemy.orm import Session
from schemas.schemas import Autoschema
from models.models import Auto


def get_car(db: Session, car_id: int):
    return db.query(Auto.car_id).filter(Auto.car_id == car_id).first()


def get_car_by_plate(db: Session, plate: str):
    return db.query(Auto.plate_number).filter(Auto.plate_number == plate).first()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Auto).offset(skip).limit(limit).all()


def create_car(db: Session, car:Autoschema):
    db.add(car)
    db.commit()
    db.refresh(car)
    return car


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
#

