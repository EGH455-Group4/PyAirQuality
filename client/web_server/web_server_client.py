'''Will hold information belonging to the implementation of the web server client.'''
import logging
import requests

from flask_restful import marshal

from client.web_server.client import Client

from models.fields import air_quality_fields
from models.models import AirQuality

class WebServerClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, web_server_address: str):
        self.web_server_address = web_server_address

        logging.info("Web server client setup.")

    def send_air_quality(self, air_quality: AirQuality):
        '''Will attempt to send air quality data.'''
        logging.info("Sending a request to web server subsystem")

        res = requests.post(self.web_server_address+"/air-quality", timeout=5, json={
            marshal(self.service.get_air_quality(), air_quality_fields)
        })

        res.close()
