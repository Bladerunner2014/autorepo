from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from constants.id_generator import IDGenerator
from datetime import datetime
from datetime import timezone

unique_id = IDGenerator("L")


class Auto(BaseModel):
    plate_number: str
    auto_name: str
    connection_status: bool = Field(default=False)
    sim_number: str = Field()
    car_model: str
    disabled: bool = Field(default=True)
    color: str
    created_at: str = Field(default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    car_id: str = Field(default=unique_id.generate_custom_id())

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


class Driver(BaseModel):
    phone_number: str
    driver_name: str
    # driver_id = Column(Integer)
    # overall_traveled_km = Column(String)
    # car_model = Column(String)
    disabled: bool = Field(default=True)
    driver_id: str = Field(default=unique_id.generate_custom_id())

    # plate_number = Column(String)
    created_at: str = Field(default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))

    # last_trip = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    # assigned_car = Column(String)
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


class Assignment(BaseModel):
    phone_number: str
    plate_number: str
    assign_id: str = Field(default=unique_id.generate_custom_id())
    active: bool = Field(default=True)
    created_by: str
    created_at: str = Field(default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }
