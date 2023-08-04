import config.config as config
import service.service
import handler.handler

def main():
    cfg = config.Config("config.json")

    srv = service.service.Service(cfg)

    hndlr = handler.handler.Handler(cfg, srv)
    hndlr.Run()

if __name__ == "__main__":
    main()