'''This file holds the models used throughout the Air Quality program.'''
import datetime

class SensorReading:
    '''Sensor reading is the generic sensor reading object.'''
    def __init__(self, reading: float, error: str):
        self.reading = reading
        self.error = error

class Sensors:
    '''Sensor is all the required sensor readings.'''
    # pylint: disable=R0913
    def __init__(self, light: SensorReading, hazardous_gases: SensorReading,
                    humidity: SensorReading, pressure: SensorReading, temperature: SensorReading):
        self.light = light
        self.hazardous_gases = hazardous_gases
        self.humidity = humidity
        self.pressure = pressure
        self.temperature = temperature

class AirQuality:
    '''Air Quality is the entire reading of the sensors with the datetime of the reading.'''
    def __init__(self, sensors: Sensors, timestamp: datetime.datetime):
        self.sensors = sensors
        self.timestamp = timestamp

class GeneralResponse:
    '''General response is the generic response object.'''
    def __init__(self, status: str):
        self.status = status
