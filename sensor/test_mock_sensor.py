'''Unit test for the mock sensor'''
import unittest

from sensor.mock_sensor import MockSensor

class TestMockSensor(unittest.TestCase):
    '''Holds all the unit tests for the mock sensor.'''

    def setUp(self):
        '''Add an instance of mock sensor to the class'''
        self.mockSen = MockSensor()

    def test_read_sensor(self):
        '''Ensure it can read the sensor'''
        reading = self.mockSen.read_sensor()

        self.assertTrue(reading.light.reading > 0)
        self.assertTrue(reading.hazardous_gases.reading > 0)
        self.assertTrue(reading.humidity.reading > 0)
        self.assertTrue(reading.pressure.reading > 0)
        self.assertTrue(reading.temperature.reading > 0)

    def test_set_lcd_screen(self):
        '''Ensure it can set the LCD screen'''
        res = self.mockSen.set_lcd_screen("temp")
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
