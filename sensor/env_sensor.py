'''Will hold information belonging to the enviro sensor.'''
from enviroplus import gas
from ltr559 import LTR559
from bme280 import BME280

from models.models import Sensors, SensorReading
from sensor.sensor import Sensor

class EnvSensor(Sensor):
    '''Implements the Sensor class, and connects to the actual hardware.'''

    def __init__(self):
        self.bme280 = BME280()
        self.ltr559 = LTR559()

    def read_sensor(self) -> Sensors:
        '''Will attempt to read the sensors.'''
        self.read_light()
        read_gas()
        self.read_humidity()
        self.read_pressure()
        self.read_temperature()

        return Sensors(
            light=SensorReading(5.5, ""),
            hazardous_gases=SensorReading(53.7, ""),
            humidity=SensorReading(89.2, ""),
            pressure=SensorReading(23.5, ""),
            temperature=SensorReading(33.2, ""),
        )

    def set_lcd_screen(self, option: str) -> bool:
        '''Will attempt to update the LCD screen on the sensor.'''
        print("ENV" + option)
        return False

    def read_light(self):
        '''Will attempt to read the light on the ltr559 sensor.'''
        print(self.ltr559.get_lux())

    def read_humidity(self):
        '''Will attempt to read the humiditiy on the bme280 sensor.'''
        print(self.bme280.get_humidity())

    def read_pressure(self):
        '''Will attempt to read the pressure on the bme280 sensor.'''
        print(self.bme280.get_pressure())

    def read_temperature(self):
        '''Will attempt to read the temperature on the bme280 sensor.'''
        print(self.bme280.get_temperature())

def read_gas():
    '''Will attempt to read the gas on the sensor.'''
    print(gas.read_all())
