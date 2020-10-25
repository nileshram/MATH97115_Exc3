# Created by nilesh at 24/10/2020
from configuration import ConfigurationFactory
import logging.config
from app.application import Application


def _configure_log():
    log_config = ConfigurationFactory.create_config("app_config.json")["log"]
    if log_config:
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    _configure_log()
    try:
        app = Application()
        app.start()
    except Exception as e:
        print(e)
