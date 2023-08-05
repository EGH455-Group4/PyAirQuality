'''Unit test for the Config class'''
import unittest

from config.config import Config

class TestConfig(unittest.TestCase):
    '''Will test the Config class'''

    def setUp(self):
        '''Add an instance of config to the class'''
        self.cfg = Config("config/test/test.json")

    def test_get_key_port(self):
        '''Ensure it can retrieve a string config'''
        self.assertEqual(self.cfg.get_key("port"), "40")

    def test_get_key_sensor_read(self):
        '''Ensure it can retrieve a int config'''
        self.assertEqual(self.cfg.get_key("sensor_read_seconds"), 78)

    def test_get_key_mock_hardware(self):
        '''Ensure it can retrieve a bool config'''
        self.assertEqual(self.cfg.get_key("mock_hardware"), False)

if __name__ == '__main__':
    unittest.main()
