# Created by nilesh at 24/10/2020

import json
from os.path import dirname, join, exists, isfile

class ConfigurationFactory:

    @staticmethod
    def create_config(file_name):
        proj_root = dirname(dirname(__file__))
        config_path = join(proj_root, "conf", file_name)
        if exists(config_path) and isfile(config_path):
            with open(config_path, "r") as f:
                app_conf = json.load(f)
        else:
            raise Exception("Config file not found please check")
        return app_conf
