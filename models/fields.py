'''This file holds the flask restful fields to help with the JSON responses.'''
from flask_restful import fields

sensor_reading_fields = {
    'value': fields.String,
    'unit': fields.String,
}

gas_reading_fields = {
    'oxidised': fields.Nested(sensor_reading_fields),
    'reduced': fields.Nested(sensor_reading_fields),
    'nh3': fields.Nested(sensor_reading_fields),
}

sensor_fields = {
    'light': fields.Nested(sensor_reading_fields),
    'hazardous_gases': fields.Nested(gas_reading_fields),
    'humidity': fields.Nested(sensor_reading_fields),
    'pressure': fields.Nested(sensor_reading_fields),
    'temperature': fields.Nested(sensor_reading_fields),
}

air_quality_fields = {
    'sensors': fields.Nested(sensor_fields),
    'timestamp': fields.DateTime(dt_format='iso8601'),
}

general_response_fields = {
    'status': fields.String,
}
