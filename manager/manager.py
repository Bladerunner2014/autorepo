from fastapi import HTTPException, status
from fastapi.responses import ORJSONResponse
from dotenv import dotenv_values
import logging
from dao.dao import Dao
from constants.info_message import InfoMessage
from constants.error_message import ErrorMessage
from schemas import schemas
from models import models

# from log import log

config = dotenv_values(".env")


# logger = logging.getLogger(__name__)


class DriverManager:
    def __init__(self):
        self.dao = Dao(config["MONGO_DB_DRIVER_COLLECTION"])

    def creator(self, driver: schemas.Driver) -> ORJSONResponse:
        check = self.dao.find_one(condition={"phone_number": driver.phone_number})
        if check:
            return ORJSONResponse(content={"message": InfoMessage.DUPLICATE_DRIVER},
                                  status_code=status.HTTP_400_BAD_REQUEST)

        res = self.dao.insert_one(document=driver.model_dump())
        # logger.info(InfoMessage.CREATE_DRIVER)

        return ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

    def reader(self, phone_number: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"phone_number": phone_number})
        if res:
            return ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

        return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

    def all(self):
        drivers = self.dao.find(condition={})
        if not drivers:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND},
                                  status_code=status.HTTP_400_BAD_REQUEST)
        return ORJSONResponse(content=drivers,
                              status_code=status.HTTP_200_OK)

    def delete(self, phone_number: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"phone_number": phone_number})
        if not res:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

        d = self.dao.delete(condition={"phone_number": phone_number})
        return ORJSONResponse(content={"message": InfoMessage.DB_DELETE}, status_code=status.HTTP_200_OK)

    def update(self, phone_number: str, new_values: dict) -> ORJSONResponse:
        res = self.dao.find_one(condition={"phone_number": phone_number})
        if not res:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

        u = self.dao.update(condition={"phone_number": phone_number}, new_values=new_values)
        return ORJSONResponse(content=u, status_code=status.HTTP_200_OK)


class AutoManager:
    def __init__(self):
        self.dao = Dao(config["MONGO_DB_AUTO_COLLECTION"])

    def creator(self, auto: schemas.Auto) -> ORJSONResponse:
        check = self.dao.find_one(condition={"plate_number": auto.plate_number})
        if check:
            return ORJSONResponse(content={"message": InfoMessage.DUPLICATE_AUTO},
                                  status_code=status.HTTP_400_BAD_REQUEST)
        res = self.dao.insert_one(document=auto.dict())
        # logger.info(InfoMessage.CREATE_AUTO)

        return ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

    def all(self):
        autos = self.dao.find(condition={})
        if not autos:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND},
                                  status_code=status.HTTP_400_BAD_REQUEST)
        return ORJSONResponse(content=autos,
                              status_code=status.HTTP_200_OK)

    def reader(self, car_plate: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"plate_number": car_plate})
        if res:
            return ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

        return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

    def delete(self, car_plate: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"plate_number": car_plate})
        if not res:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

        d = self.dao.delete(condition={"plate_number": car_plate})
        return ORJSONResponse(content={"message": InfoMessage.DB_DELETE}, status_code=status.HTTP_200_OK)

    def update(self, car_plate: str, new_values: dict) -> ORJSONResponse:
        res = self.dao.find_one(condition={"plate_number": car_plate})
        if not res:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

        u = self.dao.update(condition={"plate_number": car_plate}, new_values=new_values)
        return ORJSONResponse(content=u.raw_result, status_code=status.HTTP_200_OK)


class AssignManager:

    def __init__(self):
        self.dao = Dao(config["MONGO_DB_ASSIGN_COLLECTION"])

    def deactivate(self, assign_id: str):
        check = self.dao.find_one(condition={"assign_id": assign_id})
        if not check:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
        u = self.dao.update(condition={"assign_id": assign_id}, new_values={"active": False})
        return ORJSONResponse(content={"message": InfoMessage.DEACTIVATED}, status_code=status.HTTP_200_OK)

    def creator(self, assign: schemas.Assignment) -> ORJSONResponse:

        check = self.dao.find_one(condition={"plate_number": assign.plate_number, "phone_number": assign.phone_number})
        if check:
            return ORJSONResponse(content={"message": InfoMessage.DUPLICATE_ASSIGN},
                                  status_code=status.HTTP_400_BAD_REQUEST)
        if self.checker(plate_number=assign.plate_number, phone_number=assign.phone_number):
            res = self.dao.insert_one(document=assign.dict())
            res = ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

        else:
            res = ORJSONResponse(content={"message": ErrorMessage.DISABLED}, status_code=status.HTTP_400_BAD_REQUEST)
        # logger.info(InfoMessage.CREATE_AUTO)

        return res

    def all(self):
        assign = self.dao.find(condition={})
        if not assign:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND},
                                  status_code=status.HTTP_400_BAD_REQUEST)
        return ORJSONResponse(content=assign,
                              status_code=status.HTTP_400_BAD_REQUEST)

    def reader(self, assign_id: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"assign_id": assign_id})
        if res:
            return ORJSONResponse(content=res, status_code=status.HTTP_200_OK)

        return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

    def delete(self, assign_id: str) -> ORJSONResponse:
        res = self.dao.find_one(condition={"assign_id": assign_id})
        if not res:
            return ORJSONResponse(content={"message": InfoMessage.NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)

        d = self.dao.delete(condition={"assign_id": assign_id})
        return ORJSONResponse(content={"message": InfoMessage.DB_DELETE}, status_code=status.HTTP_200_OK)

    def checker(self, plate_number: str, phone_number: str):
        self.auto_dao = Dao(config["MONGO_DB_AUTO_COLLECTION"])
        self.driver_dao = Dao(config["MONGO_DB_DRIVER_COLLECTION"])

        p = self.auto_dao.find_one(condition={"plate_number": plate_number})
        d = self.driver_dao.find_one(condition={"phone_number": phone_number})
        if p == True or d == True:
            res = True
            return res

        return False

    # log.setup_logger()
