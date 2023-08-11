'''This will hold information about an abstract class about reading the sensor.'''
from abc import ABC, abstractmethod

from models.models import SensorReading, GasReading

class Sensor(ABC):
    '''Sensor is an abstract class that other classes will implement.'''
    @abstractmethod
    def read_light(self) -> SensorReading:
        '''Will attempt to read the light.'''

    @abstractmethod
    def read_humidity(self) -> SensorReading:
        '''Will attempt to read the humidity.'''

    @abstractmethod
    def read_pressure(self) -> SensorReading:
        '''Will attempt to read the pressure.'''

    @abstractmethod
    def read_temperature(self) -> SensorReading:
        '''Will attempt to read the temperature.'''

    @abstractmethod
    def read_gas(self) -> GasReading:
        '''Will attempt to read the gas.'''
