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

from client.image_processing.mock_image_processing_client import MockImageProcessingClient
from client.image_processing.image_processing_client import ImageProcessingClient

def main():
    '''Is the main start of the application.'''
    setup_logging()

    config = Config("config.json")

    if config.get_key("mock_hardware"):
        sensor = MockSensor()
        screen = MockScreen()
        image_processing_client = MockImageProcessingClient()
    else:
        sensor = EnvSensor(config.get_key("temperature_factor"))
        screen = EnvScreen()
        image_processing_client = ImageProcessingClient(config.get_key("image_processing_port"))

    service = Service(
        config,
        sensor,
        screen,
        local_ip(),
        image_processing_client,
    )

    background_sensor_read_thread = Thread(daemon=True, target=service.run_read_sensors)

    background_sensor_read_thread.start()

    handler = Handler(config, service)
    handler.Run()

if __name__ == "__main__":
    main()
