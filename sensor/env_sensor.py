'''Will hold information belonging to the Enviro sensor.'''
import logging

from models.models import SensorReading, GasReading
from sensor.sensor import Sensor

from helper.helper import get_cpu_temperature

class EnvSensor(Sensor):
    '''Implements the Sensor class, and connects to the actual hardware.'''

    def __init__(self, factor: float):
        from ltr559 import LTR559
        from bme280 import BME280

        self.bme280 = BME280()
        self.ltr559 = LTR559()

        self.temperature = self.bme280.get_temperature()
        self.cpu_temps = [get_cpu_temperature()] * 5

        self.factor = factor

        logging.info("Enviro sensor setup")

    def read_light(self) -> SensorReading:
        '''Will attempt to read the light on the ltr559 sensor.'''
        light_reading = self.ltr559.get_lux()
        return SensorReading(round(light_reading, 2), "Lux")

    def read_humidity(self) -> SensorReading:
        '''Will attempt to read the humidity on the bme280 sensor.'''
        humidity_reading = self.bme280.get_humidity()
        return SensorReading(round(humidity_reading, 2), "%")

    def read_pressure(self) -> SensorReading:
        '''Will attempt to read the pressure on the bme280 sensor.'''
        pressure_reading = self.bme280.get_pressure()
        return SensorReading(round(pressure_reading, 2), "hPa")

    def read_temperature(self) -> SensorReading:
        '''Will attempt to read the temperature on the bme280 sensor.'''
        raw_temperature_reading = self.bme280.get_temperature()

        cpu_temp = get_cpu_temperature()
        self.cpu_temps = self.cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
        data = raw_temperature_reading - ((avg_cpu_temp - raw_temperature_reading) / self.factor)

        self.temperature = round(data, 2)

        return SensorReading(self.temperature, "C")

    def read_gas(self) -> GasReading:
        '''Will attempt to read the gas on the sensor.'''
        from enviroplus import gas

        gas_reading = gas.read_all()

        oxidised_reading = gas_reading.oxidising / 1000
        reduced_reading = gas_reading.reducing / 1000
        ammonia_reading = gas_reading.nh3 / 1000

        return GasReading(
            oxidising_gases=SensorReading(round(oxidised_reading, 2), "kOhms"),
            reducing_gases=SensorReading(round(reduced_reading, 2), "kOhms"),
            ammonia=SensorReading(round(ammonia_reading, 2), "kOhms"),
        )
