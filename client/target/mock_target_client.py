'''Will hold information belonging to the mock target client.'''
import logging

from client.target.client import Client

class MockTargetDetectionClient(Client):
    '''Implements the Client class, but mocks results.'''

    def target_detection(self):
        '''Will just log the attempted target detection fetch.'''
        logging.info("Sent a request to target detection")
