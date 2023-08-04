import models.models as models
import sensor.sensor as sensor
import random

class MockSensor(sensor.Sensor):
    def ReadSensors(self) -> models.Sensors:
        return models.Sensors(
            light=models.SensorReading(random.random()*100, ""),
            hazardous_gases=models.SensorReading(random.random()*100, ""),
            humidity=models.SensorReading(random.random()*100, ""),
            pressure=models.SensorReading(random.random()*100, ""),
            temperature=models.SensorReading(random.random()*100, ""),
        )

    def SetLCDScreen(self, option: str):
        print("MOCK" + option)