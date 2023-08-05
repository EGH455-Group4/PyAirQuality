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
        self.srv = kwargs['srv']
        assert isinstance(self.srv, Service)

    def get(self):
        '''The HTTP GET response'''
        return marshal(self.srv.GetAirQuality(), air_quality_fields)

class SingleRead(Resource):
    '''Used to read the current air quality reading'''
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, Service)

    def get(self):
        '''The HTTP GET response'''
        return marshal(self.srv.SingleRead(), air_quality_fields)

class Start(Resource):
    '''Used to start reading the air quality'''
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, Service)

    def post(self):
        '''The HTTP POST response'''
        self.srv.Start()
        return marshal(GeneralResponse(status="OK"), general_response_fields)

class Stop(Resource):
    '''Used to stop reading the air quality'''
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, Service)

    def post(self):
        '''The HTTP POST response'''
        self.srv.Stop()
        return marshal(GeneralResponse(status="OK"), general_response_fields)

class LcdScreen(Resource):
    '''Used to alter the LCD screen on the sensor'''
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, Service)

    def post(self):
        '''The HTTP POST response'''
        json_data = request.get_json(force=True)

        display_option = json_data['display']

        if display_option not in ACCEPTABLE_LCD_DISPLAYS:
            return marshal(
                GeneralResponse(status="NOT_AN_OPTION"), general_response_fields
            ), 400

        self.srv.ChangeLCDScreen(display_option)
        return marshal(GeneralResponse(status="OK"), general_response_fields)

class Handler():
    '''Used to create the air quality server'''
    def __init__(self, cfg: Config, srv: Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(AirQuality, '/air-quality', resource_class_kwargs={'srv': srv})
        self.api.add_resource(SingleRead, '/single-read', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Start, '/start', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Stop, '/stop', resource_class_kwargs={'srv': srv})
        self.api.add_resource(LcdScreen, '/lcd-screen', resource_class_kwargs={'srv': srv})

        self.cfg = cfg

    def Run(self):
        '''Will actually run the air quality server'''
        self.app.run(debug=True, port=self.cfg.get_key("port"), host="0.0.0.0")
