import models.models as models
import sensor.sensor as sensor

class EnvSensor(sensor.Sensor):
    def ReadSensors(self) -> models.Sensors:
        return models.Sensors(
            light=models.SensorReading(5.5, ""),
            hazardous_gases=models.SensorReading(53.7, ""),
            humidity=models.SensorReading(89.2, ""),
            pressure=models.SensorReading(23.5, ""),
            temperature=models.SensorReading(33.2, ""),
        )

    def SetLCDScreen(self, option: str):
        print("ENV" + option)