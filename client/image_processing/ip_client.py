'''Will hold information belonging to the implementation of the ip client.'''
import logging
import requests

from client.image_processing.client import Client
from config.config import Config

class IPClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def current_image(self):
        '''Will attempt fetch the current ip image.'''
        logging.info("Sending a request to ip subsystem")

        ip_url = "http://127.0.0.1:" + self.cfg.get_key("ip_port")

        res = requests.post(ip_url+"/current-image", timeout=5)

        if res.status_code == 200:
            with open("./lcd_picture.jpg", 'wb') as target_disp:
                target_disp.write(res.content)

        res.close()
