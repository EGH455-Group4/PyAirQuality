'''Will hold information belonging to the implementation of the ip client.'''
import logging
import requests

from client.image_processing.client import Client

class ImageProcessingClient(Client):
    '''Implements the Client class and sends requests.'''
    def __init__(self, image_processing_port: str):
        self.image_processing_port = image_processing_port

    def current_image(self):
        '''Will attempt fetch the current ip image.'''
        logging.info("Sending a request to image processing subsystem")

        ip_url = "http://127.0.0.1:" + self.image_processing_port

        res = requests.post(ip_url+"/current-image", timeout=5)

        if res.status_code == 200:
            with open("./lcd_picture.jpg", 'wb') as image_processing_disp:
                image_processing_disp.write(res.content)

        res.close()