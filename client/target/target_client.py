'''Will hold information belonging to the implementation of the target client.'''
import logging
import requests

from client.target.client import Client
from config.config import Config

class TargetDetectionClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def target_detection(self):
        '''Will attempt fetch the current target detection.'''
        logging.info("Sending a request to target detection")

        target_url = "http://127.0.0.1:" + self.cfg.get_key("target_port")

        res = requests.post(target_url+"/target-detection", timeout=5)

        if res.status_code == 200:
            with open("./lcd_picture.jpg", 'wb') as target_disp:
                target_disp.write(res.content)

        res.close()
