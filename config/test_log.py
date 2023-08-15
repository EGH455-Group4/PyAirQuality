'''Unit test for the Log class'''
import unittest

from config.log import setup_logging

class TestConfig(unittest.TestCase):
    '''Will test the Log class'''

    def test_setup_logging_runs(self):
        '''Ensure it can retrieve a string config'''
        setup_logging(False)

if __name__ == '__main__':
    unittest.main()
