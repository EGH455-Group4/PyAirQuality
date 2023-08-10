'''Will hold information belonging to the mock sensor.'''
import random

from models.models import SensorReading, GasReading
from sensor.sensor import Sensor

class MockSensor(Sensor):
    '''Implements the Sensor class, but mocks results.'''
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

def generate_random_gas_reading() -> GasReading:
    '''Will give a random GasReading value.'''
    return GasReading(
        random_sensor_reading_between(0, 5, "kOhms"),
        random_sensor_reading_between(400, 600, "kOhms"),
        random_sensor_reading_between(40, 60, "kOhms"),
    )

def random_sensor_reading_between(lowest, highest, unit) -> SensorReading:
    '''Will give random SensorReading value.'''
    whole_value = random.randint(lowest, highest)
    decimal_value = random.random()

    generatored_value = round(float(whole_value + decimal_value), 2)

    return SensorReading(generatored_value, unit)
