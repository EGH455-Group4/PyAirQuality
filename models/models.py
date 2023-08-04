import datetime

class SensorReading:
    def __init__(self, reading: float, error: str):
        self.reading = reading
        self.error = error

class Sensors:
    def __init__(self, light: SensorReading, hazardous_gases: SensorReading,
                    humidity: SensorReading, pressure: SensorReading, temperature: SensorReading):
        self.light = light
        self.hazardous_gases = hazardous_gases
        self.humidity = humidity
        self.pressure = pressure
        self.temperature = temperature

class AirQuality:
    def __init__(self, sensors: Sensors, timestamp: datetime.datetime):
        self.sensors = sensors
        self.timestamp = timestamp

class GeneralResponse:
    def __init__(self, status: str):
        self.status = status
