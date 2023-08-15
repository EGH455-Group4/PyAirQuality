'''Service.py holds the service level functionality of the Air Quality app.'''
from datetime import datetime, timedelta
import time
import logging

from config.config import Config
from sensor.sensor import Sensor
from screen.screen import Screen
from models.models import AirQuality,Sensors,SensorReading
from models.constants import SHOW_IP_ADDRESS, SHOW_TEMPERATURE, SHOW_IMAGE_PROCESSING
from client.image_processing.client import Client

class Service():
    '''Service will have service level functions.'''
    # pylint: disable=R0902,R0913
    def __init__(
            self, config: Config, sensor: Sensor, screen: Screen, ip_address: str,
            image_processing_client: Client
        ):
        self.config = config
        self.sensor = sensor
        self.screen = screen
        self.image_processing_client = image_processing_client

        self.read_time = datetime.now()
        self.sensors = Sensors(
            temperature=SensorReading(20.0, "C")
        )

        self.screen_setting = SHOW_IP_ADDRESS
        self.ip_address = ip_address

        logging.info("Service was setup")

    def get_air_quality(self) -> AirQuality:
        '''Will give the current air quality readings.'''
        return AirQuality(self.sensors, self.read_time)

    def change_lcd_screen(self, option: str):
        '''Will update the LCD screen setting.'''
        self.screen_setting = option

        logging.info("Screen was set to %s", option)

    def run_read_sensors(self):
        '''Will loop and collect information if running.'''
        while True:
            end_time = datetime.now() + timedelta(seconds=self.config.get_key("sensor_read_seconds"))

            self.read_sensors()

            self.update_lcd_screen()

            current_time = datetime.now()

            wait_time = (end_time - current_time).total_seconds()

            if wait_time < 0:
                wait_time = 0

            time.sleep(wait_time)

    def read_sensors(self):
        '''Will collect sensor information and update read time.'''
        self.read_time = datetime.now()

        self.sensors = Sensors(
            light=self.sensor.read_light(),
            hazardous_gases=self.sensor.read_gas(),
            humidity=self.sensor.read_humidity(),
            pressure=self.sensor.read_pressure(),
            temperature=self.sensor.read_temperature(),
        )

        logging.info("Sensor was read and is: %s", self.sensors)

    def update_lcd_screen(self):
        '''Will attempt to alter the LCD screen on the sensor.'''
        if self.screen_setting == SHOW_IP_ADDRESS:
            self.screen.set_lcd_screen(self.ip_address)
        elif self.screen_setting == SHOW_TEMPERATURE:
            self.screen.set_lcd_screen(
                str(self.sensors.temperature.value) + self.sensors.temperature.unit
            )
        elif self.screen_setting == SHOW_IMAGE_PROCESSING:
            self.image_processing_client.current_image()
            self.screen.set_lcd_screen(SHOW_IMAGE_PROCESSING)
