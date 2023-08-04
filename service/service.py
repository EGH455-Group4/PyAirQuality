import config.config as config
import sensor.sensor as sensor
from datetime import datetime
import models.models as models

class Service():
    def __init__(self, cfg: config.Config, snr: sensor.Sensor):
        self.cfg = cfg
        self.snr = snr
        self.running = False
        self.read_time = datetime.now()
        self.sensors = models.Sensors(
            light=models.SensorReading(0, ""),
            hazardous_gases=models.SensorReading(0, ""),
            humidity=models.SensorReading(0, ""),
            pressure=models.SensorReading(0, ""),
            temperature=models.SensorReading(0, ""),
        )

    def Start(self):
        print("start")

    def Stop(self):
        print("stop")

    def GetAirQuality(self) -> models.AirQuality:
        return models.AirQuality(self.sensors, self.read_time)

    def SingleRead(self) -> models.AirQuality:
        self.readSensors

        return models.AirQuality(self.sensors, self.read_time)

    def ChangeLCDScreen(self, option: str):
        print(option)

    def readSensors(self):
        self.read_time = datetime.now()

        self.sensors = self.snr.ReadSensors()