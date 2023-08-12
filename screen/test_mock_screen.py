'''Unit test for the mock screen'''
import unittest

from screen.mock_screen import MockScreen

class TestMockScreen(unittest.TestCase):
    '''Holds all the unit tests for the mock screen.'''

    def setUp(self):
        '''Add an instance of mock screen to the class'''
        self.mock_screen = MockScreen()

    def test_set_lcd_screen(self):
        '''Ensure it can retrieve a string config'''
        self.mock_screen.set_lcd_screen("TEST")

if __name__ == '__main__':
    unittest.main()
