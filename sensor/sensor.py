import models.models as models
from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def ReadSensors(self) -> models.Sensors:
        pass

    @abstractmethod
    def SetLCDScreen(self, option: str):
        pass