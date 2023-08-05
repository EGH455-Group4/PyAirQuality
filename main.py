'''main.py is the main entrypoint to the Air Quality application.'''
from threading import Thread

from config.config import Config
from service.service import Service
from handler.handler import Handler
from helper.helper import local_ip
from sensor.env_sensor import EnvSensor
from sensor.mock_sensor import MockSensor
from screen.mock_screen import MockScreen
from screen.env_screen import EnvScreen

def main():
    '''Is the main start of the application.'''
    print(local_ip())

    cfg = Config("config.json")

    if cfg.get_key("mock_hardware"):
        snr = MockSensor()
        scre = MockScreen()
    else:
        snr = EnvSensor(cfg.get_key("temperature_factor"))
        scre = EnvScreen()

    srv = Service(cfg, snr, scre)

    background_sensor_read_thread = Thread(daemon=True, target=srv.run_read_sensors)

    background_sensor_read_thread.start()

    hndlr = Handler(cfg, srv)
    hndlr.Run()

if __name__ == "__main__":
    main()
