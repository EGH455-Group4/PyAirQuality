import config.config as config
import service.service as service
import models.models as models
import models.constants as constants
import models.fields as fields
from flask import Flask, request
from flask_restful import Resource, Api, marshal

class AirQuality(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, service.Service)

    def get(self):
        return marshal(self.srv.GetAirQuality(), fields.air_quality_fields)

class SingleRead(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, service.Service)

    def get(self):
        return marshal(self.srv.SingleRead(), fields.air_quality_fields)

class Start(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, service.Service)

    def post(self):
        self.srv.Start()
        return marshal(models.GeneralResponse(status="OK"), fields.general_response_fields)

class Stop(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, service.Service)

    def post(self):
        self.srv.Stop()
        return marshal(models.GeneralResponse(status="OK"), fields.general_response_fields)

class LcdScreen(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']
        assert isinstance(self.srv, service.Service)

    def post(self):
        json_data = request.get_json(force=True)

        display_option = json_data['display']

        if display_option not in constants.ACCEPTABLE_LCD_DISPLAYS:
             return marshal(models.GeneralResponse(status="NOT_AN_OPTION"), fields.general_response_fields), 400

        self.srv.ChangeLCDScreen(display_option)
        return marshal(models.GeneralResponse(status="OK"), fields.general_response_fields)

class Handler():
    def __init__(self, cfg: config.Config, srv: service.Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(AirQuality, '/air-quality', resource_class_kwargs={'srv': srv})
        self.api.add_resource(SingleRead, '/single-read', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Start, '/start', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Stop, '/stop', resource_class_kwargs={'srv': srv})
        self.api.add_resource(LcdScreen, '/lcd-screen', resource_class_kwargs={'srv': srv})

        self.cfg = cfg

    def Run(self):
        self.app.run(debug=True, port=self.cfg.GetKey("port"))
