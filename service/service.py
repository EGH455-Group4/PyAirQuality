import config.config as config
import sensor.sensor as sensor
from datetime import datetime
import models.models as models
import time

class Service():
    def __init__(self, cfg: config.Config, snr: sensor.Sensor):
        self.cfg = cfg
        self.snr = snr
        self.running = True
        self.read_time = datetime.now()
        self.sensors = models.Sensors(
            light=models.SensorReading(0, ""),
            hazardous_gases=models.SensorReading(0, ""),
            humidity=models.SensorReading(0, ""),
            pressure=models.SensorReading(0, ""),
            temperature=models.SensorReading(0, ""),
        )

    def Start(self):
        self.resetVars()

        self.running = True

    def Stop(self):
        self.running = False

        self.resetVars()

    def GetAirQuality(self) -> models.AirQuality:
        return models.AirQuality(self.sensors, self.read_time)

    def SingleRead(self) -> models.AirQuality:
        self.readSensors()

        return models.AirQuality(self.sensors, self.read_time)

    def ChangeLCDScreen(self, option: str):
        self.ChangeLCDScreen(option)

    def RunReadSensors(self):
        while True:
            if self.running:
                self.readSensors()

            time.sleep(2)

    def readSensors(self):
        self.read_time = datetime.now()

        self.sensors = self.snr.ReadSensors()

    def resetVars(self):
        self.read_time = datetime.now()
        self.sensors = models.Sensors(
            light=models.SensorReading(0, ""),
            hazardous_gases=models.SensorReading(0, ""),
            humidity=models.SensorReading(0, ""),
            pressure=models.SensorReading(0, ""),
            temperature=models.SensorReading(0, ""),
        )