'''Will hold information belonging to the mock sample client.'''
import logging

from client.sample.client import Client

class MockSampleClient(Client):
    '''Implements the Client class, but mocks results.'''

    def sample(self):
        '''Will just log the attempted sample request.'''
        logging.info("Sent a request to sample tube ")