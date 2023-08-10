'''This will hold information about an abstract class about sending requests to the sampling tube system.'''
from abc import ABC, abstractmethod

class Client(ABC):
    '''Client is an abstract class that other classes will implement.'''
    @abstractmethod
    def sample(self):
        '''Will tell the sampling tube to sample.'''