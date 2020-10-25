# Created by nilesh at 24/10/2020
import sys
from os.path import dirname
from configuration import ConfigurationFactory
import logging.config
from app.application import Application


def _configure_log():
    log_config = ConfigurationFactory.create_config("app_config.json")["log"]
    if log_config:
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(level=logging.DEBUG)

#add src to PYTHONPATH
def _configure_env():
    root_dir = dirname(__file__)
    sys.path.append(root_dir)

if __name__ == "__main__":
    _configure_log()
    _configure_env()
    try:
        app = Application()
        app.start()
    except Exception as e:
        print(e)
