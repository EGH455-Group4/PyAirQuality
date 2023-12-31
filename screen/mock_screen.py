'''Will hold information belonging to the mock LCD screen.'''
import logging

from screen.screen import Screen

class MockScreen(Screen):
    '''Implements the Screen class, and connects to mocked hardware.'''
    def __init__(self):
        logging.info("Mock screen setup")

    def set_lcd_screen(self, message: str):
        '''Will log out the set message.'''
        logging.info("Mock screen was set to - %s", message)
