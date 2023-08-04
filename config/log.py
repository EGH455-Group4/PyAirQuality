import json, logging, sys, datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        extra = getattr(record, "__dict__", {})

        json_record = {
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "level": getattr(record, "levelname", None),
            "file": getattr(record, "filename", None),
            "line": getattr(record, "lineno", None),
            "message": getattr(record, "msg", None),
            "additional_detail": extra.get("additional_detail"),
        }
        return json.dumps(json_record)

def JsonConfig():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    logging.getLogger().addHandler(handler)
