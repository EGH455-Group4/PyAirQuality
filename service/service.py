import config.config as config

class Service():
    def __init__(self, cfg: config.Config):
        self.cfg = cfg

    def Start(self):
        print("start")

    def Stop(self):
        print("stop")