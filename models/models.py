from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from datetime import timezone
Base = declarative_base()


class Auto(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True, index=True)
    auto_name = Column(String)
    connection_status = Column(Boolean)
    sim_number = Column(Integer)
    car_id = Column(String)
    car_model = Column(String)
    disabled = Column(Boolean)
    plate_number = Column(String)
    created_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    last_active_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    assigned_to = Column(String)
