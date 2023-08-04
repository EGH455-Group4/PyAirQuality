from flask_restful import fields

sensor_reading_fields = {
    'reading': fields.String,
    'error': fields.String,
}

sensor_fields = {
    'light': fields.Nested(sensor_reading_fields),
    'hazardous_gases': fields.Nested(sensor_reading_fields),
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