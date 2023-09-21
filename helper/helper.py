'''This file will hold all the helper functions that are required for the Air Quality app.'''
import socket
import random
import math

from models.models import SensorReading, GasReading, IndividualGasReading
from models.constants import BASELINE_REDUCING, BASELINE_OXIDISING, BASELINE_NH3, PPM

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
    '''Will convert kOhms to ppm values'''
    oxidising_ppm = math.pow(10, math.log10(
        raw_values.oxidising_gases.value/BASELINE_OXIDISING
    ) - 0.8129)

    if oxidising_ppm < 0:
        oxidising_ppm = 0.01

    reducing_ppm = math.pow(10, -1.25 * math.log10(
        raw_values.reducing_gases.value/BASELINE_REDUCING
    ) + 0.64)

    if reducing_ppm < 0:
        reducing_ppm = 0.01

    nh3_ppm = math.pow(10, -1.8 * math.log10(
        raw_values.nh3.value/BASELINE_NH3
    ) - 0.163)

    if nh3_ppm < 0:
        nh3_ppm = 0.01

    return GasReading(
        oxidising_gases=SensorReading(
            round(oxidising_ppm, 2),
            PPM,
        ), reducing_gases=SensorReading(
            round(reducing_ppm, 2),
            PPM,
        ), nh3=SensorReading(
            round(nh3_ppm, 2),
            PPM,
        )
    )

def create_individual_gases(raw_values: GasReading) -> IndividualGasReading:
    '''Will create individual gases object'''
    oxidising_ratio = raw_values.oxidising_gases.value/BASELINE_OXIDISING
    reducing_ratio = raw_values.reducing_gases.value/BASELINE_REDUCING
    nh3_ratio = raw_values.nh3.value/BASELINE_NH3

    carbon_monoxide = log_equation(-0.656, reducing_ratio, 2.6955)

    nitrogen_dioxide = linear_equation(6.933, oxidising_ratio, -0.1866)

    ethanol = average([
        log_equation(-0.245, reducing_ratio, 1.0991), log_equation(-0.098, nh3_ratio, 0.5232)
    ])

    hydrogen = average([
        log_equation(-0.176, reducing_ratio, 0.7992), \
        log_equation(-0.067, oxidising_ratio, 1.1687), log_equation(-0.168, nh3_ratio, 1.1908)
    ])

    ammonia = average([
        log_equation(-0.14, reducing_ratio, 0.9591), log_equation(-0.158, nh3_ratio, 0.7157)
    ])

    methane = log_equation(-0.154, reducing_ratio, 1.9652)

    propane = average([
        log_equation(-0.076, reducing_ratio, 0.7787), log_equation(-0.232, nh3_ratio, 2.388)
    ])

    iso_butane = log_equation(-0.205, nh3_ratio, 2.1054)

    return IndividualGasReading(
        carbon_monoxide=SensorReading(
            carbon_monoxide,
            PPM
        ), nitrogen_dioxide=SensorReading(
            nitrogen_dioxide,
            PPM,
        ), ethanol=SensorReading(
            ethanol,
            PPM,
        ), hydrogen=SensorReading(
            hydrogen,
            PPM,
        ), ammonia=SensorReading(
            ammonia,
            PPM,
        ), methane=SensorReading(
            methane,
            PPM,
        ), propane=SensorReading(
            propane,
            PPM,
        ), iso_butane=SensorReading(
            iso_butane,
            PPM,
        )
    )

def linear_equation(m_value, x_value, c_value):
    '''Will calculate a log equation, giving a small value if negative'''
    value = m_value * x_value + c_value

    if value < 0:
        value = 0.01

    return round(value, 2)

def log_equation(m_value, x_value, c_value):
    '''Will calculate a log equation, giving a small value if negative'''
    value = m_value * math.log(x_value) + c_value

    if value < 0:
        value = 0.01

    return round(value, 2)

def average(values):
    '''Will calculate an average of a list, rounding it to 2 decimal places'''
    total = sum(values)

    avg = total / len(values)

    return round(avg, 2)
