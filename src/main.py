# Created by nilesh at 24/10/2020
from pydoc import locate
import sys
from os.path import dirname
from argparse import ArgumentParser
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

def _configure_cmdline():
    cmd_conf = ConfigurationFactory.create_config("app_config.json")["cmd_line_args"]
    parser = ArgumentParser(description=cmd_conf["desc"])
    for cmd in cmd_conf["args"]:
        parser.add_argument(cmd_conf["args"][cmd]["name"],
                            help=cmd_conf["args"][cmd]["help"],
                            type=locate(cmd_conf["args"][cmd]["type"]))
    args = parser.parse_args()

if __name__ == "__main__":
    _configure_log()
    _configure_env()
    _configure_cmdline()
    try:
        app = Application()
        app.start()
    except Exception as e:
        print(e)
