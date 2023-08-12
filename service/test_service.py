'''Unit test for the service'''
import unittest
from unittest.mock import Mock, create_autospec, patch

from service.service import Service
from config.config import Config
from screen.screen import Screen
from sensor.sensor import Sensor
from client.image_processing.client import Client

from models.models import AirQuality, Sensors, SensorReading, GasReading

class TestService(unittest.TestCase):
    '''Holds all the unit tests for the service.'''

    def setUp(self):
        '''Sets up the mocks for the test case'''
        self.mockCfg = create_autospec(Config)

        self.mockSensor = create_autospec(Sensor)
        self.mockScreen = create_autospec(Screen)

        self.mockClient = create_autospec(Client)

        self.service = Service(
            self.mockCfg,
            self.mockSensor,
            self.mockScreen,
            "192.0.0.1",
            self.mockClient,
        )

    def test_get_air_quality(self):
        '''Ensure it can get the air quality'''
        res = self.service.get_air_quality()

        self.assertIsInstance(res, AirQuality)
        self.assertEqual(
            res.sensors.temperature.value,
            20.0
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

        self.mockScreen.set_lcd_screen.assert_called_with("192.0.0.1")

    def test_read_sensors(self):
        '''Ensure it can read the sensors'''
        self.mockSensor.read_light.return_value = SensorReading(
            value=23.2,
            unit="lux"
        )

        self.mockSensor.read_humidity.return_value = SensorReading(
            value=32.1,
            unit="%"
        )

        self.mockSensor.read_pressure.return_value = SensorReading(
            value=2,
            unit="hPa"
        )

        self.mockSensor.read_temperature.return_value = SensorReading(
            value=11.2,
            unit="C"
        )

        self.mockSensor.read_gas.return_value = GasReading(
            oxidised=SensorReading(
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
            self.service.sensors.hazardous_gases.oxidised.value,
            55.2
        )
        self.assertEqual(
            self.service.sensors.hazardous_gases.oxidised.unit,
            "kOhms"
        )

if __name__ == '__main__':
    unittest.main()
