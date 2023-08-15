'''Will hold information belonging to the mock sensor.'''
import logging

from helper.helper import random_sensor_reading_between, generate_random_gas_reading
from models.models import SensorReading, GasReading
from sensor.sensor import Sensor

class MockSensor(Sensor):
    '''Implements the Sensor class, but mocks results.'''
    def __init__(self):
        logging.info("Mock sensor setup")

    def read_light(self) -> SensorReading:
        '''Will give a random light reading.'''
        return random_sensor_reading_between(10, 20, "lux")

    def read_humidity(self) -> SensorReading:
        '''Will give a random humidity reading.'''
        return random_sensor_reading_between(20, 40, "%")

    def read_pressure(self) -> SensorReading:
        '''Will give a random pressure reading.'''
        return random_sensor_reading_between(900, 1100, "hPa")

    def read_temperature(self) -> SensorReading:
        '''Will give a random temperature reading.'''
        return random_sensor_reading_between(10, 30, "C")

    def read_gas(self) -> GasReading:
        '''Will give a random gas reading.'''
        return generate_random_gas_reading()
