'''This will hold information about an abstract class about reading the sensor.'''
from abc import ABC, abstractmethod

from models.models import Sensors

class Sensor(ABC):
    '''Sensor is an abstract class that other classes will implement.'''
    @abstractmethod
    def read_sensor(self) -> Sensors:
        '''Will read the sensors in implementations.'''
