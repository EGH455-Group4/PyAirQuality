'''This file will hold all the helper functions that are required for the Air Quality app.'''
import socket
import random

from models.models import SensorReading, GasReading

def local_ip():
    '''Will attempt to get the computer's IP on the local internet.'''
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_connection.connect(("8.8.8.8", 80))
    ip_address = socket_connection.getsockname()[0]
    socket_connection.detach()
    return ip_address

def get_cpu_temperature():
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
