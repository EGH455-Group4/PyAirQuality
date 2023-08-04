import json

class Config:
    def __init__(self, location: str):
        self.config = json.load(open(location))

    def GetKey(self, key: str):
        return self.config[key]