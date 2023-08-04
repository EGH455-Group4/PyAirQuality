import config.config as config
import service.service as service
import handler.handler as handler
import sensor.sensor as sensor

def main():
    cfg = config.Config("config.json")

    snrs = sensor.Sensor()

    srv = service.Service(cfg, snrs)

    hndlr = handler.Handler(cfg, srv)
    hndlr.Run()

if __name__ == "__main__":
    main()