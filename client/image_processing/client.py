'''This will hold information about an abstract class designed to sending requests
to the image processing subsystem.'''
from abc import ABC, abstractmethod

class Client(ABC):
    '''Client is an abstract class that other classes will implement.'''
    @abstractmethod
    def current_image(self):
        '''Will attempt fetch the current image of the image processing system.'''
