# Created by nilesh at 24/10/2020

from computation.stats import StatsEngine
from graph.lib import Scatter, Histogram
import logging

class Application:

    def __init__(self):
        self._logger = logging.getLogger("stats_log")
        self._init_states()
        self._init_components()

    def _init_states(self):
        self.started = None
        self.stopped = True

    def _init_components(self):
        self._logger.info("Initialising Stats Components")
        self.stats_engine = StatsEngine()

    def _init_graphs(self, data):
        self._graphs = {"scatter" : Scatter(data), "histogram" : Histogram(data)}

    def start(self):
        self._logger.debug("Starting Stats Application")
        self.started = True
        self.stopped = False
        try:
            self.stats_engine.generate_samples()
            self.stats_engine.generate_ecdf()
            self._init_graphs(self.stats_engine)
        except Exception as e:
            print(str(e))

    def stop(self):
        pass

