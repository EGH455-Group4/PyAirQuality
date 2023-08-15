'''This file holds the models used throughout the Air Quality program.'''
import datetime

class SensorReading:
    '''Sensor reading is the generic sensor reading object.'''
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self) -> str:
        return f"{0}{1}".format(self.value, self.unit)

class GasReading:
    '''GasReading is a specific sensor reading of the hazardous_gases'''
    def __init__(self, oxidising_gases: SensorReading = None, reducing_gases: SensorReading = None,
                ammonia: SensorReading = None):
        self.oxidising_gases = oxidising_gases
        self.reducing_gases = reducing_gases
        self.ammonia = ammonia

    def __str__(self) -> str:
        return f"oxidising_gases: {0}, reducing_gases: {1}, ammonia: {2}".format(
            self.oxidising_gases, self.reducing_gases, self.ammonia,
        )

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

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"light: {0}, gas_reading: {1}, humidity: {2}, pressure: {3}, temperature: {4}.".format(
            self.light, self.hazardous_gases, self.humidity, self.pressure, self.temperature,
        )

class AirQuality:
    '''Air Quality is the entire reading of the sensors with the datetime of the reading.'''
    def __init__(self, sensors: Sensors, timestamp: datetime.datetime):
        self.sensors = sensors
        self.timestamp = timestamp

class GeneralResponse:
    '''General response is the generic response object.'''
    def __init__(self, status: str):
        self.status = status
