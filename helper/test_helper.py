'''Unit test for the helper functions'''
import unittest

from helper.helper import (local_ip, get_cpu_temperature, random_sensor_reading_between,
                           generate_random_gas_reading)

class TestHelpers(unittest.TestCase):
    '''Holds all the unit tests for the helper functions'''
    def test_local_ip(self):
        '''Ensure it can retrieve a string version of the IP'''
        res = local_ip()
        self.assertTrue(isinstance(res, str))
        self.assertTrue(res != "")
        # pylint: disable=W1401
        self.assertRegex(res, "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    def test_get_cpu_temperature(self):
        '''Ensure it can retrieve the CPU temp'''
        res = get_cpu_temperature()
        self.assertTrue(isinstance(res, float))
        self.assertGreater(res, -256)

    def test_generate_random_gas_reading(self):
        '''Ensure it can generate a random gas reading'''
        res = generate_random_gas_reading()
        self.assertGreater(res.oxidised.value, 0)
        self.assertLess(res.oxidised.value, 6)
        self.assertEqual(res.oxidised.unit, "kOhms")

    def test_random_sensor_reading_between(self):
        '''Ensure it can generate a random sensor reading'''
        res = random_sensor_reading_between(9, 10, "unit")
        self.assertGreater(res.value, 8)
        self.assertLess(res.value, 11)
        self.assertEqual(res.unit, "unit")

if __name__ == '__main__':
    unittest.main()
