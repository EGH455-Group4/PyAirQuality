'''Service.py holds the service level functionality of the Air Quality app.'''
from datetime import datetime
import time

from config.config import Config
from sensor.sensor import Sensor
from screen.screen import Screen
from models.models import AirQuality,Sensors,SensorReading
from models.constants import SHOW_IP_ADDRESS, SHOW_TEMPERATURE, SHOW_TARGET_DETECTION

from client.image_processing.client import Client as IPClient

SAMPLE_THRESHOLD = 0.3

class Service():
    '''Service will have service level functions.'''
    # pylint: disable=R0902,R0913
    def __init__(
            self,cfg: Config, snr: Sensor, scr: Screen, ip_addr: str,
            image_processing_client: IPClient
        ):
        self.cfg = cfg
        self.snr = snr
        self.scr = scr
        self.image_processing_client = image_processing_client

        self.read_time = datetime.now()
        self.sensors = Sensors(
            temperature=SensorReading(20.0, "C")
        )

        self.screen_setting = SHOW_IP_ADDRESS
        self.ip_addr = ip_addr

    def get_air_quality(self) -> AirQuality:
        '''Will give the current air quality readings.'''
        return AirQuality(self.sensors, self.read_time)

    def change_lcd_screen(self, option: str):
        '''Will update the LCD screen setting.'''
        self.screen_setting = option

    def run_read_sensors(self):
        '''Will loop and collect information if running.'''
        while True:
            self.read_sensors()

            self.update_lcd_screen()

            time.sleep(self.cfg.get_key("sensor_read_seconds"))

    def read_sensors(self):
        '''Will collect sensor information and update read time.'''
        self.read_time = datetime.now()

        self.sensors = Sensors(
            light=self.snr.read_light(),
            hazardous_gases=self.snr.read_gas(),
            humidity=self.snr.read_humidity(),
            pressure=self.snr.read_pressure(),
            temperature=self.snr.read_temperature(),
        )

    def update_lcd_screen(self):
        '''Will attempt to alter the LCD screen on the sensor.'''
        if self.screen_setting == SHOW_IP_ADDRESS:
            self.scr.set_lcd_screen(self.ip_addr)
        elif self.screen_setting == SHOW_TEMPERATURE:
            self.scr.set_lcd_screen(
                str(self.sensors.temperature.value) + self.sensors.temperature.unit
            )
        elif self.screen_setting == SHOW_TARGET_DETECTION:
            self.target_client.target_detection()
            self.scr.set_lcd_screen(SHOW_TARGET_DETECTION)
