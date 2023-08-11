'''Handler will showcase the Air Quality endpoints'''
from flask import Flask, request
from flask_restful import Resource, Api, marshal

from config.config import Config
from service.service import Service
from models.models import GeneralResponse
from models.constants import ACCEPTABLE_LCD_DISPLAYS
from models.fields import air_quality_fields, general_response_fields

class AirQuality(Resource):
    '''Used to retrieve the current air quality reading'''
    def __init__(self, **kwargs):
        self.service = kwargs['service']
        assert isinstance(self.service, Service)

    def get(self):
        '''The HTTP GET response'''
        return marshal(self.service.get_air_quality(), air_quality_fields)

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
            ), 400

        self.service.change_lcd_screen(display_option)
        return marshal(GeneralResponse(status="OK"), general_response_fields)

class Handler():
    '''Used to create the air quality server'''
    def __init__(self, config: Config, service: Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(AirQuality, '/air-quality', resource_class_kwargs={
            'service': service
        })
        self.api.add_resource(LcdScreen, '/lcd-screen', resource_class_kwargs={
            'service': service
        })

        self.config = config

    def Run(self):
        '''Will actually run the air quality server'''
        self.app.run(debug=False, port=self.config.get_key("port"), host="0.0.0.0")
