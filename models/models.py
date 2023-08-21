'''This file holds the models used throughout the Air Quality program.'''

class SensorReading(dict):
    '''Sensor reading is the generic sensor reading object.'''
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

        dict.__init__(self, value=value, unit=unit)

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"

class GasReading(dict):
    '''GasReading is a specific sensor reading of the hazardous_gases'''
    def __init__(self, oxidising_gases: SensorReading = None, reducing_gases: SensorReading = None,
                ammonia: SensorReading = None):
        self.oxidising_gases = oxidising_gases
        self.reducing_gases = reducing_gases
        self.ammonia = ammonia

        dict.__init__(self, oxidising_gases=oxidising_gases, reducing_gases=reducing_gases, \
                      ammonia=ammonia)

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"oxidising_gases: {self.oxidising_gases}, reducing_gases: {self.reducing_gases}, ammonia: {self.ammonia}"

class Sensors(dict):
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

        dict.__init__(self, light=light, hazardous_gases=hazardous_gases, humidity=humidity, \
                      pressure=pressure, temperature=temperature)

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"light: {self.light}, gas_reading: {self.hazardous_gases}, humidity: {self.humidity}, pressure: {self.pressure}, temperature: {self.temperature}."

class AirQuality(dict):
    '''Air Quality is the entire reading of the sensors with the datetime of the reading.'''
    def __init__(self, sensors: Sensors, timestamp: str):
        self.sensors = sensors
        self.timestamp = timestamp

        dict.__init__(self, sensors=sensors, timestamp=timestamp)

class GeneralResponse:
    '''General response is the generic response object.'''
    def __init__(self, status: str):
        self.status = status
