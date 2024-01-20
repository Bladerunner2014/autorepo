from pydantic import BaseModel


class Autoschema(BaseModel):
    auto_name: str
    connection_status: bool | None = None
    sim_number: int
    car_id: str | None = None
    car_model: str
    disabled: bool | None = None
    plate_number: str
    created_at: str | None = None
    last_active_at: str | None = None
    assigned_to: str | None = None

    class Config:
        orm_mode = True
