'''This will hold information about an abstract class designed to sending requests
to the web server system.'''
from abc import ABC, abstractmethod

from models.models import AirQuality

class Client(ABC):
    '''Client is an abstract class that other classes will implement.'''
    @abstractmethod
    def send_air_quality(self, air_quality: AirQuality):
        '''Will attempt to send the current air quality reading to the server.'''
