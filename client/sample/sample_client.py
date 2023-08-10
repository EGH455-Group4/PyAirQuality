'''Will hold information belonging to the sample client.'''
import logging

from client.sample.client import Client

class SampleClient(Client):
    '''Implements the Client class and sends requests.'''

    def sample(self):
        '''Will just log the attempted sample request.'''
        logging.info("Sent a request to sample tube ")