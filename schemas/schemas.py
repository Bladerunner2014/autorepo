from pydantic import BaseModel


class Auto(BaseModel):
    auto_name: str
    connection_status: bool | None = None
    sim_number: int
    car_model: str
    disabled: bool | None = None
    plate_number: str
    color: str | None = None

    class Config:
        orm_mode = True


class Driver(BaseModel):
    driver_name: str
    # driver_id: int
    # connection_status: bool | None = None
    phone_number: int
    # overall_traveled_km: int | None = None
    # car_model: str
    disabled: bool | None = None

    # plate_number: str
    # created_at: str | None = None

    # last_trip: str | None = None
    # assigned_car: str | None = None
    class Config:
        orm_mode = True


class Assignment(BaseModel):
    plate_number: str
    phone_number: int
    created_by: str

    class Config:
        orm_mode = True
