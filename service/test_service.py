'''Unit test for the service'''
import unittest
from unittest.mock import create_autospec

from service.service import Service
from config.config import Config
from screen.screen import Screen
from sensor.sensor import Sensor
from client.image_processing.client import Client as IPClient
from client.web_server.client import Client as WSClient

from models.models import AirQuality, SensorReading, GasReading

class TestService(unittest.TestCase):
    '''Holds all the unit tests for the service.'''

    def setUp(self):
        '''Sets up the mocks for the test case'''
        self.mock_cfg = create_autospec(Config)

        self.mock_sensor = create_autospec(Sensor)
        self.mock_screen = create_autospec(Screen)

        self.mock_ip_client = create_autospec(IPClient)
        self.mock_ws_client = create_autospec(WSClient)

        self.service = Service(
            self.mock_cfg,
            self.mock_sensor,
            self.mock_screen,
            "192.0.0.1",
            self.mock_ip_client,
            self.mock_ws_client,
        )

    def test_change_lcd_screen(self):
        '''Ensure it can set the lcd screen'''
        self.service.change_lcd_screen("TEST")

        self.assertEqual(
            self.service.screen_setting,
            "TEST"
        )

    def test_update_lcd_screen(self):
        '''Ensure it can update the lcd screen'''
        self.service.update_lcd_screen()

        self.mock_screen.set_lcd_screen.assert_called_with("192.0.0.1")

    def test_read_sensors(self):
        '''Ensure it can read the sensors'''
        self.mock_sensor.read_light.return_value = SensorReading(
            value=23.2,
            unit="lux"
        )

        self.mock_sensor.read_humidity.return_value = SensorReading(
            value=32.1,
            unit="%"
        )

        self.mock_sensor.read_pressure.return_value = SensorReading(
            value=2,
            unit="hPa"
        )

        self.mock_sensor.read_temperature.return_value = SensorReading(
            value=11.2,
            unit="C"
        )

        self.mock_sensor.read_gas.return_value = GasReading(
            oxidising_gases=SensorReading(
                value=55.2,
                unit="kOhms"
            )
        )

        self.service.read_sensors()

        self.assertEqual(
            self.service.sensors.light.value,
            23.2
        )
        self.assertEqual(
            self.service.sensors.light.unit,
            "lux"
        )

        self.assertEqual(
            self.service.sensors.humidity.value,
            32.1
        )
        self.assertEqual(
            self.service.sensors.humidity.unit,
            "%"
        )

        self.assertEqual(
            self.service.sensors.pressure.value,
            2
        )
        self.assertEqual(
            self.service.sensors.pressure.unit,
            "hPa"
        )

        self.assertEqual(
            self.service.sensors.temperature.value,
            11.2
        )
        self.assertEqual(
            self.service.sensors.temperature.unit,
            "C"
        )

        self.assertEqual(
            self.service.sensors.hazardous_gases.oxidising_gases.value,
            55.2
        )
        self.assertEqual(
            self.service.sensors.hazardous_gases.oxidising_gases.unit,
            "kOhms"
        )

if __name__ == '__main__':
    unittest.main()
