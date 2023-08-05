'''Will hold information belonging to the mock LCD screen.'''
from screen.screen import Screen

class MockScreen(Screen):
    '''Implements the Screen class, and connects to mock hardware.'''

    def set_lcd_screen(self, option: str) -> bool:
        '''Will log out the set option.'''
        print("MOCK" + option)
        return True
