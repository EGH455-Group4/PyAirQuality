'''Config will be used to configure the PyAirQuality application.'''
import json
from dataclasses import dataclass

@dataclass
class Config:
    '''Config is a class to hold the configuration'''
    def __init__(self, location: str):
        with open(location, 'r', encoding="utf8") as file:
            self.config = json.load(file)
            file.close()

    def get_key(self, key: str) -> any:
        '''get_key is used to retrieve specific configuration'''
        return self.config[key]
