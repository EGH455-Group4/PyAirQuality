'''Will hold information belonging to the implementation of the web server client.'''
import json
import logging

import requests

from client.web_server.client import Client

from models.models import AirQuality

class WebServerClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, web_server_address: str):
        self.web_server_address = web_server_address

        logging.info("Web server client setup.")

    def send_air_quality(self, air_quality: AirQuality):
        '''Will attempt to send air quality data.'''
        logging.info("Sending a request to web server subsystem")
        try:
            res = requests.post(self.web_server_address+"/air-quality", timeout=5, json={
                "air_quality": json.dumps(air_quality)
            }, headers={'Content-Type': 'application/json'})

            res.close()
        except Exception as error:
            logging.error("failed to send data to web server %s", error)
