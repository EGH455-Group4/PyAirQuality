'''Will hold information belonging to the mock web server client.'''
import logging

from client.web_server.client import Client

from models.models import AirQuality

class MockWebServerClient(Client):
    '''Implements the Client class, but mocks results.'''
    def __init__(self):
        logging.info("Mock web server client setup.")

    def send_air_quality(self, air_quality: AirQuality):
        '''Will just log the attempted send air quality data.'''
        logging.info("Sent a request to the MOCKED web server subsystem")
