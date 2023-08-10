'''Will hold information belonging to the implementation of the target client.'''
import logging

from client.target.client import Client

class TargetDetectionClient(Client):
    '''Implements the Client class and sends requests.'''

    def target_detection(self):
        '''Will attempt fetch the current target detection.'''
        logging.info("Sent a request to target detection")
