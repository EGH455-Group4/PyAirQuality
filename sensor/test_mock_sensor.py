'''Unit test for the mock sensor'''
import unittest

from sensor.mock_sensor import MockSensor

class TestMockSensor(unittest.TestCase):
    '''Holds all the unit tests for the mock sensor.'''

    def setUp(self):
        '''Add an instance of mock sensor to the class'''
        self.mock_sen = MockSensor()

    def test_read_sensor(self):
        '''Ensure it can read the sensor'''
        reading = self.mock_sen.read_sensor()

        self.assertTrue(reading.light.value > 0)
        self.assertTrue(reading.hazardous_gases.value > 0)
        self.assertTrue(reading.humidity.value > 0)
        self.assertTrue(reading.pressure.value > 0)
        self.assertTrue(reading.temperature.value > 0)

if __name__ == '__main__':
    unittest.main()
