'''This file holds the models used throughout the Air Quality program.'''
import datetime

class SensorReading:
    '''Sensor reading is the generic sensor reading object.'''
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

class GasReading:
    '''GasReading is a specific sensor reading of the hazardous_gases'''
    def __init__(self, oxidised: SensorReading = None, reduced: SensorReading = None,
                nh3: SensorReading = None):
        self.oxidised = oxidised
        self.reduced = reduced
        self.nh3 = nh3

class Sensors:
    '''Sensor is all the required sensor readings.'''
    # pylint: disable=R0913
    def __init__(self, light: SensorReading = None, hazardous_gases: GasReading = None,
                    humidity: SensorReading = None, pressure: SensorReading = None,
                    temperature: SensorReading = None):
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
