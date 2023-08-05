'''Will hold information belonging to the enviro sensor.'''
from models.models import Sensors, SensorReading
from sensor.sensor import Sensor

class EnvSensor(Sensor):
    '''Implements the Sensor class, and connects to the actual hardware.'''
    def read_sensor(self) -> Sensors:
        '''Will attempt to read the sensors.'''
        return Sensors(
            light=SensorReading(5.5, ""),
            hazardous_gases=SensorReading(53.7, ""),
            humidity=SensorReading(89.2, ""),
            pressure=SensorReading(23.5, ""),
            temperature=SensorReading(33.2, ""),
        )

    def set_lcd_screen(self, option: str):
        '''Will attempt to update the LCD screen on the sensor.'''
        print("ENV" + option)
