'''Will hold information belonging to the sample client.'''
import logging
import requests

from client.sample.client import Client
from config.config import Config

class SampleClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def sample(self):
        '''Will log the attempted sample request and send it.'''
        logging.info("Sending a request to sample tube")

        sample_url = "http://127.0.0.1:" + self.cfg.get_key("sample_port")

        res = requests.post(sample_url+"/sample", timeout=5)

        logging.info(res.content)

        res.close()
