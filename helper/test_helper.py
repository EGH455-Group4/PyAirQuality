'''Unit test for the helper funcs'''
import unittest

from helper.helper import local_ip

class TestHelpers(unittest.TestCase):
    '''Holds all the unit tests for the helper funcs'''
    def test_local_ip(self):
        '''Ensure it can retrieve a string version of the IP'''
        res = local_ip()
        self.assertTrue(isinstance(res, str))
        self.assertTrue(res != "")

if __name__ == '__main__':
    unittest.main()
