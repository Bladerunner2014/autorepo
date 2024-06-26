from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from constants.id_generator import IDGenerator
from datetime import datetime
from datetime import timezone

unique_id = IDGenerator("L")


class Service(BaseModel):
    service_id: str = Field(default_factory=unique_id.generate_custom_id)
    title: str
    service_description: Optional[str] = None
    cost_per_service: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))

    def __init__(self, **data):
        super().__init__(**data)
        self.service_id = unique_id.generate_custom_id()
        self.created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")


class Auto(BaseModel):
    plate_number: str
    auto_name: str
    connection_status: bool = Field(default=False)
    sim_number: str = Field()
    car_model: str
    disabled: bool = Field(default=True)
    color: str
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    car_id: str = Field(default_factory=unique_id.generate_custom_id)  # Pass the method without calling it
    def __init__(self, **data):
        super().__init__(**data)
        self.car_id = unique_id.generate_custom_id()
        self.created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")

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
    driver_id: str = Field(default_factory=unique_id.generate_custom_id)

    # plate_number = Column(String)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))

    # last_trip = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    # assigned_car = Column(String)
    def __init__(self, **data):
        super().__init__(**data)
        self.driver_id = unique_id.generate_custom_id()
        self.created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")

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
