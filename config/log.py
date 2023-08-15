'''This module will setup the python logging.'''
import logging

def setup_logging(log_to_file: bool):
    '''This function will setup the python logging standard for the application.'''
    if log_to_file:
        logging.basicConfig(
            filename="log.txt",
            filemode="w",
            format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        return

    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
