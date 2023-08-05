'''Will hold information belonging to the enviro sensor.'''
from enviroplus import gas
from ltr559 import LTR559
from bme280 import BME280

from models.models import Sensors, SensorReading, GasReading
from sensor.sensor import Sensor

class EnvSensor(Sensor):
    '''Implements the Sensor class, and connects to the actual hardware.'''

    def __init__(self, factor: float):
        self.bme280 = BME280()
        self.ltr559 = LTR559()
        self.temperature = self.bme280.get_temperature()
        self.cpu_temps = [get_cpu_temperature()] * 5
        self.factor = factor

    def read_sensor(self) -> Sensors:
        '''Will attempt to read the sensors.'''
        light_sensor_reading = self.read_light()
        gas_sensor_reading = read_gas()
        humidity_sensor_reading = self.read_humidity()
        pressure_sensor_reading = self.read_pressure()
        temperature_sensor_reading = self.read_temperature()

        return Sensors(
            light=light_sensor_reading,
            hazardous_gases=gas_sensor_reading,
            humidity=humidity_sensor_reading,
            pressure=pressure_sensor_reading,
            temperature=temperature_sensor_reading,
        )

    def read_light(self) -> SensorReading:
        '''Will attempt to read the light on the ltr559 sensor.'''
        light_reading = self.ltr559.get_lux()
        return SensorReading(round(light_reading, 2), "Lux")

    def read_humidity(self) -> SensorReading:
        '''Will attempt to read the humiditiy on the bme280 sensor.'''
        humidity_reading = self.bme280.get_humidity()
        return SensorReading(round(humidity_reading, 2), "%")

    def read_pressure(self):
        '''Will attempt to read the pressure on the bme280 sensor.'''
        pressure_reading = self.bme280.get_pressure()
        return SensorReading(round(pressure_reading, 2), "hPa")

    def read_temperature(self):
        '''Will attempt to read the temperature on the bme280 sensor.'''
        raw_temperature_reading = self.bme280.get_temperature()

        cpu_temp = get_cpu_temperature()
        self.cpu_temps = self.cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
        data = raw_temperature_reading - ((avg_cpu_temp - raw_temperature_reading) / self.factor)

        self.temperature = round(data, 2)

        return SensorReading(self.temperature, "C")

def read_gas():
    '''Will attempt to read the gas on the sensor.'''
    gas_reading = gas.read_all()

    oxidised_reading = gas_reading.oxidising / 1000
    reduced_reading = gas_reading.reducing / 1000
    nh3_reading = gas_reading.nh3 / 1000

    return GasReading(
        oxidised=SensorReading(round(oxidised_reading, 2), "kOhms"),
        reduced=SensorReading(round(reduced_reading, 2), "kOhms"),
        nh3=SensorReading(round(nh3_reading, 2), "kOhms"),
    )

def get_cpu_temperature():
    '''get_cpu_temperature will attempt to read the current cpu temperature in C'''
    with open("/sys/class/thermal/thermal_zone0/temp", "r", encoding="utf8") as temperature_file:
        temp = temperature_file.read()
        temp = int(temp) / 1000.0
    return temp
