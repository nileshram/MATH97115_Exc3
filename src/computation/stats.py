# Created by nilesh at 24/10/2020

import numpy as np
from configuration import ConfigurationFactory
import logging

class StatsEngine:

    def __init__(self):
        self._logger = logging.getLogger("stats_log")
        self._init_conf()
        self._init_params()

    def _init_conf(self):
        self.config = ConfigurationFactory.create_config("app_config.json")

    def _init_params(self):
        self.exp_params = self.config["exp_cdf"]
        self._logger.info("Initialised random samples {}".format(self.exp_params["random_samples"]))

    def generate_samples(self):
        """ Generates random samples from the configuration file"""
        self.exp_sample = {}
        for sample_sze in self.exp_params["random_samples"]:
            # generate random samples from the config
            exp_rv = np.sort(np.random.exponential(1 / self.exp_params["lambda"],
                                                   sample_sze))
            # append the results
            self.exp_sample[sample_sze] = exp_rv
            self._logger.debug("Successfully generated exponential random sample of size {}".format(sample_sze))
        return self.exp_sample

    def generate_ecdf(self):
        self.ecdf = {}
        for sze, sample in self.exp_sample.items():
            x = np.sort(sample)
            n = x.size
            y = np.arange(1, n + 1) / n
            self.ecdf[sze] = {"x": sample, "y": y}
            self._logger.debug("Successfully generated exponential cdf sample of size {}".format(sze))
        return self.ecdf

    def __str__(self):
        return "StatsEngine generating random variables from exponential distribution with" \
               "lambda = {}".format(self.exp_params["lambda"])
