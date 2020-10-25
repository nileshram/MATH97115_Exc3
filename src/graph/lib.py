# Created by nilesh at 25/10/2020

import matplotlib.pyplot as plt
import logging
import numpy as np

class Graph:

    def __init__(self):
        """Construct Figure and Axes Objects"""
        self.figure, self.axes = plt.subplots()
        self.axes.set_facecolor('#E6E6E6') #set bg to grey
        self.axes.grid(linestyle='-', linewidth='0.5', color='white')

    def add_plot_title(self, chart_title, **kwargs):
        self.axes.set_title(str(chart_title), **kwargs)

    def add_x_axis_title(self, x_axis_title):
        self.axes.set_xlabel(str(x_axis_title))

    def add_y_axis_title(self, y_axis_title):
        self.axes.set_ylabel(str(y_axis_title))

    def add_x_ticks(self, x_tick_list):
        self.axes.set_xticks(x_tick_list)

    def add_y_ticks(self, y_tick_list):
        self.axes.set_yticks(y_tick_list)

    def add_x_ticks_label(self, x_ticks_label, **kwargs):
        """kwargs include: minor=False, rotation=90"""
        self.axes.set_xticklabels(x_ticks_label, **kwargs)

    def add_y_ticks_label(self, y_ticks_label, **kwargs):
        """kwargs include: minor=False"""
        self.axes.set_yticklabels(y_ticks_label, **kwargs)

class Scatter(Graph):

    def __init__(self, data):
        super(Scatter, self).__init__()
        self._logger = logging.getLogger("stats_log")
        self.plot_scatter(data)
        self.display()

    def add_charting_labels(self):
        plt.xlabel('x - (Exponential R.V.)')
        plt.ylabel('Probability')
        plt.title("ECDF Plot for Exponential Random Samples")
        plt.legend()

    def plot_scatter(self, data):
        self._logger.info("Plotting scatter graph of ecdf for all samples")
        for sample_sze in data.ecdf:
            #plot the scatter graph
            self.axes.scatter(data.ecdf[sample_sze]["x"],
                              data.ecdf[sample_sze]["y"],
                              s=10,
                              edgecolors='black',
                              alpha=0.5,
                              label="n = {}".format(sample_sze))
        self.add_charting_labels()

    def display(self):
        plt.show()

class Histogram(Graph):

    def __init__(self, data):
        super(Histogram, self).__init__()
        self._logger = logging.getLogger("stats_log")
        self.plot_hist(data)
        self.display()

    def plot_hist(self, data):
        self._logger.info("Plotting histogram for all sample sizes")
        for sample_sze in data.exp_sample:
            #plot the scatter graph
            self.axes.hist(np.sort(data.exp_sample[sample_sze]),
                           bins=100,
                           edgecolor="black",
                           alpha=0.5,
                           label="n = {}".format(sample_sze))
        self.add_charting_labels()

    def add_charting_labels(self):
        plt.xlabel('x - Exponential R.V.')
        plt.ylabel('Density')
        plt.title("Density Plot for Exponential Random Variables")
        plt.legend()

    def display(self):
        plt.show()