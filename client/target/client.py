'''This will hold information about an abstract class about sending requests
to the target detection.'''
from abc import ABC, abstractmethod

class Client(ABC):
    '''Client is an abstract class that other classes will implement.'''
    @abstractmethod
    def target_detection(self):
        '''Will attempt fetch the current target detection.'''
