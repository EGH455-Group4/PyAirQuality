'''Service.py holds the service level functionality of the Air Quality app.'''
from datetime import datetime, timedelta
import time
import logging

from config.config import Config
from sensor.sensor import Sensor
from screen.screen import Screen
from models.models import AirQuality,Sensors,SensorReading
from models.constants import SHOW_IP_ADDRESS, SHOW_TEMPERATURE, SHOW_IMAGE_PROCESSING
from client.image_processing.client import Client as IPClient
from client.web_server.client import Client as WSClient
from helper.helper import gas_to_ppm_conversion, create_individual_gases

class Service():
    '''Service will have service level functions.'''
    # pylint: disable=R0902,R0913
    def __init__(
            self, config: Config, sensor: Sensor, screen: Screen, ip_address: str,
            image_processing_client: IPClient, web_server_client: WSClient,
            send_raw_gas_values: bool,
        ):
        self.config = config
        self.sensor = sensor
        self.screen = screen
        self.image_processing_client = image_processing_client
        self.web_server_client = web_server_client
        self.send_raw_gas_values = send_raw_gas_values

        self.read_time = datetime.now()
        self.sensors = Sensors(
            temperature=SensorReading(20.0, "C")
        )

        self.screen_setting = SHOW_IP_ADDRESS
        self.ip_address = ip_address
        self.ip_address_set = False

        logging.info("Service was setup")

    def send_air_quality(self) -> AirQuality:
        '''Will send out the current air quality readings.'''
        self.web_server_client.send_air_quality(
            AirQuality(self.sensors, self.read_time.isoformat(sep="T",timespec="auto"))
        )

    def change_lcd_screen(self, option: str):
        '''Will update the LCD screen setting.'''
        self.screen_setting = option

        self.ip_address_set = False

        logging.info("Screen was set to %s", option)

    def run_read_sensors(self):
        '''Will loop and collect information if running.'''
        while True:
            end_time = datetime.now() + timedelta(
                seconds=self.config.get_key("sensor_read_seconds")
            )

            self.read_sensors()

            self.send_air_quality()

            self.update_lcd_screen()

            current_time = datetime.now()

            wait_time = max((end_time - current_time).total_seconds(), 0)

            time.sleep(wait_time)

    def read_sensors(self):
        '''Will collect sensor information and update read time.'''
        self.read_time = datetime.now()

        gas_values = self.sensor.read_gas()

        gas_individual_values = None

        if not self.send_raw_gas_values:
            gas_individual_values = create_individual_gases(raw_values=gas_values)
            gas_values = gas_to_ppm_conversion(raw_values=gas_values)

        self.sensors = Sensors(
            light=self.sensor.read_light(),
            hazardous_gases=gas_values,
            humidity=self.sensor.read_humidity(),
            pressure=self.sensor.read_pressure(),
            temperature=self.sensor.read_temperature(),
            individual_gases=gas_individual_values,
        )

        logging.info("Sensor was read and is: %s", self.sensors)

    def update_lcd_screen(self):
        '''Will attempt to alter the LCD screen on the sensor.'''
        if self.screen_setting == SHOW_IP_ADDRESS and not self.ip_address_set:
            self.screen.set_lcd_screen(self.ip_address)
            self.ip_address_set = True
        elif self.screen_setting == SHOW_TEMPERATURE:
            self.screen.set_lcd_screen(
                str(self.sensors.temperature.value) + self.sensors.temperature.unit
            )
        elif self.screen_setting == SHOW_IMAGE_PROCESSING:
            self.image_processing_client.current_image()
            self.screen.set_lcd_screen(SHOW_IMAGE_PROCESSING)
