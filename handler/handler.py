'''Handler will showcase the Air Quality endpoints'''
import logging
from flask import Flask, request
from flask_restful import Resource, Api, marshal

from config.config import Config
from service.service import Service
from models.models import GeneralResponse
from models.constants import ACCEPTABLE_LCD_DISPLAYS
from models.fields import general_response_fields

class LcdScreen(Resource):
    '''Used to alter the LCD screen on the sensor'''
    def __init__(self, **kwargs):
        self.service = kwargs['service']
        assert isinstance(self.service, Service)

    def post(self):
        '''The HTTP POST response'''
        json_data = request.get_json(force=True)

        display_option = json_data['display']

        if display_option not in ACCEPTABLE_LCD_DISPLAYS:
            return marshal(
                GeneralResponse(status="NOT_AN_OPTION"), general_response_fields
            ), {'Access-Control-Allow-Origin': '*'}

        self.service.change_lcd_screen(display_option)
        return marshal(GeneralResponse(status="OK"), general_response_fields), \
            {'Access-Control-Allow-Origin': '*'}

class Handler():
    '''Used to create the air quality server'''
    def __init__(self, config: Config, service: Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(LcdScreen, '/lcd-screen', resource_class_kwargs={
            'service': service
        })

        self.config = config

        logging.info("Handler was setup.")

    def Run(self):
        '''Will actually run the air quality server'''
        self.app.run(debug=False, port=self.config.get_key("port"), host="0.0.0.0")
