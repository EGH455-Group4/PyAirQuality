'''Will hold information belonging to the mock sensor.'''
import random

from models.models import Sensors, SensorReading, GasReading
from sensor.sensor import Sensor

class MockSensor(Sensor):
    '''Implements the Sensor class, but mocks results.'''
    def read_sensor(self) -> Sensors:
        '''Will give random readings.'''
        return Sensors(
            light=random_sensor_reading_between(10, 20, "lux"),
            hazardous_gases=generate_random_gas_reading(),
            humidity=random_sensor_reading_between(20, 40, "%"),
            pressure=random_sensor_reading_between(900, 1100, "hPa"),
            temperature=random_sensor_reading_between(10, 30, "C"),
        )

def generate_random_gas_reading() -> GasReading:
    return GasReading(
        random_sensor_reading_between(0, 5, "kOhms"),
        random_sensor_reading_between(400, 600, "kOhms"),
        random_sensor_reading_between(40, 60, "kOhms"),
    )

def random_sensor_reading_between(lowest, highest, unit) -> SensorReading:
    whole_value = random.randint(lowest, highest)
    decimal_value = random.random()

    generatored_value = round(float(whole_value + decimal_value), 2)

    return SensorReading(generatored_value, unit)