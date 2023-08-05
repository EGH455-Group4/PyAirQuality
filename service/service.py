'''Service.py holds the service level functionality of the Air Quality app.'''
from datetime import datetime
import time

from config.config import Config
from sensor.sensor import Sensor
from models.models import AirQuality,Sensors,SensorReading

class Service():
    '''Service will have service level functions.'''
    def __init__(self, cfg: Config, snr: Sensor):
        self.cfg = cfg
        self.snr = snr
        self.running = True
        self.read_time = datetime.now()
        self.sensors = Sensors(
            light=SensorReading(0, ""),
            hazardous_gases=SensorReading(0, ""),
            humidity=SensorReading(0, ""),
            pressure=SensorReading(0, ""),
            temperature=SensorReading(0, ""),
        )

    def start(self):
        '''Will reset vars and will enable the service to start collecting information.'''
        self.reset_vars()

        self.running = True

    def stop(self):
        '''Will reset vars and will disable the service from collecting information.'''
        self.running = False

        self.reset_vars()

    def get_air_quality(self) -> AirQuality:
        '''Will give the current air quality readings.'''
        return AirQuality(self.sensors, self.read_time)

    def single_read(self) -> AirQuality:
        '''Will run the read sensor function and give the current air quality readings.'''
        self.read_sensors()

        return AirQuality(self.sensors, self.read_time)

    def change_lcd_screen(self, option: str):
        '''Will attempt to alter the LCD screen on the sensor.'''
        self.snr.set_lcd_screen(option)

    def run_read_sensors(self):
        '''Will loop and collect information if running.'''
        while True:
            if self.running:
                self.read_sensors()

            time.sleep(self.cfg.get_key["sensor_read_seconds"])

    def read_sensors(self):
        '''Will collect sensor information and update read time.'''
        self.read_time = datetime.now()

        self.sensors = self.snr.read_sensor()

    def reset_vars(self):
        '''Will reset the current sensor information.'''
        self.read_time = datetime.now()
        self.sensors = Sensors(
            light=SensorReading(0, ""),
            hazardous_gases=SensorReading(0, ""),
            humidity=SensorReading(0, ""),
            pressure=SensorReading(0, ""),
            temperature=SensorReading(0, ""),
        )
