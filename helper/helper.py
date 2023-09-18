'''This file will hold all the helper functions that are required for the Air Quality app.'''
import socket
import random
import math

from models.models import SensorReading, GasReading
from models.constants import BASELINE_REDUCING, BASELINE_OXIDISING, BASELINE_NH3

def local_ip() -> str:
    '''Will attempt to get the computer's IP on the local internet.'''
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_connection.connect(("8.8.8.8", 80))
    ip_address = socket_connection.getsockname()[0]
    socket_connection.detach()
    return ip_address

def get_cpu_temperature() -> float:
    '''get_cpu_temperature will attempt to read the current cpu temperature in C'''
    with open("/sys/class/thermal/thermal_zone0/temp", "r", encoding="utf8") as temperature_file:
        temperature = temperature_file.read()
        temperature = int(temperature) / 1000.0
    return temperature


def generate_random_gas_reading() -> GasReading:
    '''Will give a random GasReading value.'''
    return GasReading(
        random_sensor_reading_between(0, 5, "kOhms"),
        random_sensor_reading_between(400, 600, "kOhms"),
        random_sensor_reading_between(40, 60, "kOhms"),
    )

def random_sensor_reading_between(lowest, highest, unit) -> SensorReading:
    '''Will give random SensorReading value.'''
    whole_value = random.randint(lowest, highest)
    decimal_value = random.random()

    generated_value = round(float(whole_value + decimal_value), 2)

    return SensorReading(generated_value, unit)

def gas_to_ppm_conversion(raw_values: GasReading):
    oxidising_ppm = math.pow(10, math.log10(
        raw_values.oxidising_gases.value/BASELINE_OXIDISING
    ) - 0.8129)

    reducing_ppm = math.pow(10, -1.25 * math.log10(
        raw_values.reducing_gases.value/BASELINE_REDUCING
    ) + 0.64)

    nh3_ppm = math.pow(10, -1.8 * math.log10(
        raw_values.nh3.value/BASELINE_NH3
    ) - 0.163)

    return GasReading(
        oxidising_gases=SensorReading(
            round(oxidising_ppm, 2),
            "ppm",
        ), reducing_gases=SensorReading(
            round(reducing_ppm, 2),
            "ppm",
        ), nh3=SensorReading(
            round(nh3_ppm, 2),
            "ppm",
        )
    )