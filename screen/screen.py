'''This will hold information about an abstract class about the LCD screen.'''
from abc import ABC, abstractmethod

class Screen(ABC):
    '''Screen is an abstract class that other classes will implement.'''

    @abstractmethod
    def set_lcd_screen(self, option: str) -> bool:
        '''Will alter the LCD screen in implementations.'''
