'''Will hold information belonging to the mock sensor.'''
import random

from models.models import Sensors, SensorReading
from sensor.sensor import Sensor

class MockSensor(Sensor):
    '''Implements the Sensor class, but mocks results.'''
    def read_sensor(self) -> Sensors:
        '''Will give random readings.'''
        return Sensors(
            light=SensorReading(random.random()*100, ""),
            hazardous_gases=SensorReading(random.random()*100, ""),
            humidity=SensorReading(random.random()*100, ""),
            pressure=SensorReading(random.random()*100, ""),
            temperature=SensorReading(random.random()*100, ""),
        )

    def set_lcd_screen(self, option: str) -> bool:
        '''Will log out the set option.'''
        print("MOCK" + option)
        return True
