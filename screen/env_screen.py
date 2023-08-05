'''Will hold information belonging to the enviro LCD screen.'''
from screen.screen import Screen

class EnvScreen(Screen):
    '''Implements the Screen class, and connects to the actual hardware.'''

    def set_lcd_screen(self, option: str) -> bool:
        '''Will log out the set option.'''
        print("ENVIRO" + option)
        return True