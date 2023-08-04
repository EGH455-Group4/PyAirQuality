import models.models as models

class Sensor():
    def ReadSensors(self) -> models.Sensors:
        return models.Sensors(
            light=models.SensorReading(2.3, ""),
            hazardous_gases=models.SensorReading(53.7, ""),
            humidity=models.SensorReading(89.2, ""),
            pressure=models.SensorReading(23.5, ""),
            temperature=models.SensorReading(33.2, ""),
        )