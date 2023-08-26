'''This script is a standalone command which will update the LCD screen to the IP address'''
import logging

from config.config import Config
from config.log import setup_logging
from service.service import Service
from helper.helper import local_ip

from screen.mock_screen import MockScreen
from screen.env_screen import EnvScreen

def main():
    '''Is the main start of the command.'''
    config = Config("config.json")

    setup_logging(config.get_key("log_to_file"))

    if config.get_key("mock_hardware"):
        screen = MockScreen()
    else:
        screen = EnvScreen()

    local_ip_address = local_ip()

    logging.info("ip address is %s", local_ip_address)

    if local_ip_address == "":
        exit(1)

    service = Service(
        config,
        None,
        screen,
        local_ip_address,
        None,
        None,
    )

    service.update_lcd_screen()

    exit(0)

if __name__ == "__main__":
    main()

