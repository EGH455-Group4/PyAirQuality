'''Unit test for the mock sensor'''
import unittest

from sensor.mock_sensor import MockSensor

class TestMockSensor(unittest.TestCase):
    '''Holds all the unit tests for the mock sensor.'''

    def setUp(self):
        '''Add an instance of mock sensor to the class'''
        self.mock_sensor = MockSensor()

    def test_read_light(self):
        '''Ensure it can retrieve a light reading'''
        res = self.mock_sensor.read_light()
        self.assertGreater(res.value, 9)
        self.assertLess(res.value, 21)
        self.assertEqual(res.unit, "lux")

    def test_read_humidity(self):
        '''Ensure it can retrieve a humidity reading'''
        res = self.mock_sensor.read_humidity()
        self.assertGreater(res.value, 19)
        self.assertLess(res.value, 41)
        self.assertEqual(res.unit, "%")

    def test_read_pressure(self):
        '''Ensure it can retrieve a pressure reading'''
        res = self.mock_sensor.read_pressure()
        self.assertGreater(res.value, 899)
        self.assertLess(res.value, 1101)
        self.assertEqual(res.unit, "hPa")

    def test_read_temperature(self):
        '''Ensure it can retrieve a temperature reading'''
        res = self.mock_sensor.read_temperature()
        self.assertGreater(res.value, 9)
        self.assertLess(res.value, 31)
        self.assertEqual(res.unit, "C")

    def test_read_gas(self):
        '''Ensure it can retrieve a gas reading'''
        res = self.mock_sensor.read_gas()

        self.assertGreater(res.oxidised.value, -1)
        self.assertLess(res.oxidised.value, 6)
        self.assertEqual(res.oxidised.unit, "kOhms")

        self.assertGreater(res.reduced.value, 399)
        self.assertLess(res.reduced.value, 601)
        self.assertEqual(res.reduced.unit, "kOhms")

        self.assertGreater(res.nh3.value, 39)
        self.assertLess(res.nh3.value, 61)
        self.assertEqual(res.nh3.unit, "kOhms")

if __name__ == '__main__':
    unittest.main()
