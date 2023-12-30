from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.orm_database import Base


class Auto(Base):
    __tablename__ = "auto"
    id = Column(Integer, primary_key=True, index=True)

    auto_name = Column(String)
    connection_status = Column(Boolean)
    sim_number = Column(Integer)
    car_id = Column(String)
    car_model = Column(String)
    disabled = Column(Boolean)
    plate_number = Column(Integer)
    created_at = Column(String)
    last_active_at = Column(String)


model_config = {"form_name": "vehicle", "form_id": "None", "action": "add, update, delete, get", "payload": "None"}

# class Auto(BaseModel):
#     auto_name: str
#     connection_status: bool | None = None
#     sim_number: str
#     car_id: str | None = None
#     car_model: str
#     disabled: bool | None = None
#     plate_number: str
#     passwordConfirm: str
#     created_at: datetime | None = None
#     last_active_at: datetime | None = None
#
#     class Config:
#         orm_mode = True
