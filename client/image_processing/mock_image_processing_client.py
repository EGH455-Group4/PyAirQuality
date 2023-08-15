'''Will hold information belonging to the mock ip client.'''
import logging

from client.image_processing.client import Client

class MockImageProcessingClient(Client):
    '''Implements the Client class, but mocks results.'''
    def __init__(self):
        logging.info("Mock image processing client setup.")

    def current_image(self):
        '''Will just log the attempted fetch for image processing image.'''
        logging.info("Sent a request to the MOCKED image processing subsystem")
