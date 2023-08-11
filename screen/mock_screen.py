'''Will hold information belonging to the mock LCD screen.'''
import logging

from screen.screen import Screen

class MockScreen(Screen):
    '''Implements the Screen class, and connects to mocked hardware.'''

    def set_lcd_screen(self, message: str):
        '''Will log out the set message.'''
        logging.info("MOCK SCREEN WAS SET TO - %s", message)
        return True
