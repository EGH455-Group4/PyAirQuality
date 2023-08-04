import config.config as config
import service.service as service
from flask import Flask
from flask_restful import Resource, Api

class AirQuality(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']

    def get(self):
        return {'hello': 'world'}

class SingleRead(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']

    def get(self):
        return {'hello': 'world'}

class Start(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']

    def post(self):
        return {}

class Stop(Resource):
    def __init__(self, **kwargs):
        self.srv = kwargs['srv']

    def post(self):
        self.srv.Stop()
        return {}

class Handler():
    def __init__(self, cfg: config.Config, srv: service.Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        srv.Stop()

        self.api.add_resource(AirQuality, '/air-quality', resource_class_kwargs={'srv': srv})
        self.api.add_resource(SingleRead, '/single-read', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Start, '/start', resource_class_kwargs={'srv': srv})
        self.api.add_resource(Stop, '/stop', resource_class_kwargs={'srv': srv})

        self.cfg = cfg

    def Run(self):
        self.app.run(debug=True, port=self.cfg.GetKey("port"))
