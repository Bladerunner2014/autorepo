from datetime import datetime
from pydantic import BaseModel


class Autoschema(BaseModel):
    auto_name: str
    connection_status: bool | None = None
    sim_number: str
    car_id: str | None = None
    car_model: str
    disabled: bool | None = None
    plate_number: str
    passwordConfirm: str
    created_at: datetime | None = None
    last_active_at: datetime | None = None

    class Config:
        orm_mode = True
