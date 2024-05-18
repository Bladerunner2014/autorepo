from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from constants.id_generator import IDGenerator
from datetime import datetime
from datetime import timezone

Base = declarative_base()
unique_id = IDGenerator("L")


class Auto(Base):
    __tablename__ = "auto"
    plate_number = Column(String, primary_key=True, index=True)
    auto_name = Column(String)
    connection_status = Column(Boolean)
    sim_number = Column(Integer)
    car_model = Column(String)
    disabled = Column(Boolean)
    color = Column(String)
    created_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    car_id = Column(String, default=unique_id.prefix)
    # last_active_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    # assigned_to = Column(String)


class Driver(Base):
    __tablename__ = "drivers"
    phone_number = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String)
    # driver_id = Column(Integer)
    # overall_traveled_km = Column(String)
    # car_model = Column(String)
    disabled = Column(Boolean)
    driver_id = Column(String, default=unique_id.prefix)

    # plate_number = Column(String)
    created_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    # last_trip = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
    # assigned_car = Column(String)


class Assignment(Base):
    __tablename__ = "assignment"
    phone_number = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, primary_key=True, index=True)
    assign_id = Column(String, default=unique_id.prefix)
    active = Column(Boolean, default=True)
    created_by = Column(String, primary_key=True, index=True)
    created_at = Column(String, default=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))
