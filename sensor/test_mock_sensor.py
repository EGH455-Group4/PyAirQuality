'''Unit test for the mock sensor'''
import unittest

from sensor.mock_sensor import MockSensor

class TestMockSensor(unittest.TestCase):
    '''Holds all the unit tests for the mock sensor.'''

    def setUp(self):
        '''Add an instance of mock sensor to the class'''
        self.mock_sen = MockSensor()

if __name__ == '__main__':
    unittest.main()
