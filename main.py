'''main.py is the main entrypoint to the Air Quality application.'''
from threading import Thread

from config.config import Config
from config.log import setup_logging
from service.service import Service
from handler.handler import Handler
from helper.helper import local_ip

from sensor.env_sensor import EnvSensor
from sensor.mock_sensor import MockSensor
from screen.mock_screen import MockScreen
from screen.env_screen import EnvScreen

from client.target.mock_target_client import MockTargetDetectionClient
from client.target.target_client import TargetDetectionClient
from client.sample.mock_sample_client import MockSampleClient
from client.sample.sample_client import SampleClient

def main():
    '''Is the main start of the application.'''
    setup_logging()

    cfg = Config("config.json")

    if cfg.get_key("mock_hardware"):
        snr = MockSensor()
        scre = MockScreen()
        sample_client = MockSampleClient()
        target_client = MockTargetDetectionClient()
    else:
        snr = EnvSensor(cfg.get_key("temperature_factor"))
        scre = EnvScreen()
        sample_client = SampleClient()
        target_client = TargetDetectionClient()

    srv = Service(
        cfg,
        snr,
        scre,
        local_ip(),
        sample_client,
        target_client,
    )

    background_sensor_read_thread = Thread(daemon=True, target=srv.run_read_sensors)

    background_sensor_read_thread.start()

    hndlr = Handler(cfg, srv)
    hndlr.Run()

if __name__ == "__main__":
    main()
