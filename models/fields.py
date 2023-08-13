'''This file holds the flask restful fields to help with the JSON responses.'''
from flask_restful import fields

sensor_reading_fields = {
    'value': fields.Float,
    'unit': fields.String,
}

gas_reading_fields = {
    'oxidising_gases': fields.Nested(sensor_reading_fields),
    'reducing_gases': fields.Nested(sensor_reading_fields),
    'ammonia': fields.Nested(sensor_reading_fields),
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
