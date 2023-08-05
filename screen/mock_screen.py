'''Will hold information belonging to the mock LCD screen.'''
from screen.screen import Screen

class MockScreen(Screen):
    '''Implements the Screen class, and connects to mock hardware.'''

    def set_lcd_screen(self, message: str) -> bool:
        '''Will log out the set message.'''
        print("MOCK" + message)
        return True