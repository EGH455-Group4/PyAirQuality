import config.config as config
import service.service as service
import handler.handler as handler
import sensor.sensor, sensor.env_sensor, sensor.mock_sensor
from threading import Thread

def main():
    cfg = config.Config("config.json")

    if cfg.GetKey("mock_hardware"):
        snr = sensor.mock_sensor.MockSensor()
    else:
        snr = sensor.env_sensor.EnvSensor()

    srv = service.Service(cfg, snr)

    backgroundSensorReads = Thread(daemon=True, target=srv.RunReadSensors)

    backgroundSensorReads.start()

    hndlr = handler.Handler(cfg, srv)
    hndlr.Run()

if __name__ == "__main__":
    main()