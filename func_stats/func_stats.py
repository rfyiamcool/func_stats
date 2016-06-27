from __future__ import print_function

from collections import OrderedDict
from time import time
from .prettytable import PrettyTable

import inspect

class CreateStats(OrderedDict):

    def __init__(self):
        super(CreateStats, self).__init__()
        self['_start'] = time()
        self.last_mark = self['_start']
        self.auto_increment = 1
        self.marker_code = {}

    def point(self, marker_name=None, current_frame=None):

        if marker_name is None:
            marker_name = self.auto_increment
            self.auto_increment += 1

        if not self.get(marker_name):
            self[marker_name] = []

        time_elapsed = time() - self.last_mark
        self.last_mark = time()

        self[marker_name].append(time_elapsed)
        if current_frame is None:
            current_frame = inspect.currentframe()
        last_frame = current_frame.f_back
        self.marker_code[marker_name] = (
            last_frame.f_code.co_filename,
            last_frame.f_lineno,
            last_frame.f_code.co_name
        )


    def stop(self):
        self['_end'] = time()

    def display(self):
        x = PrettyTable(["Marker", "Method", "Line", "Hits", "Avg Time", "Runtime", "Percent"])
        x.align["Marker"] = "l"
        x.align["Hits"] = "r"
        x.align["Avg Time"] = "r"
        x.align["Runtime"] = "r"
        x.align["Percent"] = "r"
        x.align["Method"] = "l"
        x.align["Line"] = "r"
        x.padding_width = 1
        if '_end' not in self:
            self['_end'] = time()
        total_time = self['_end'] - self['_start']
        for marker, runtimes in self.items():
            if type(runtimes) is not list:
                continue
            x.add_row((
                marker,
                self.marker_code[marker][2],
                self.marker_code[marker][1],
                len(runtimes),
                "{0:.5f}".format(sum(runtimes) / float(len(runtimes))),
                "{0:.5f}".format(sum(runtimes)),
                "{0:.2f}".format(sum(runtimes) / total_time * 100),
            ))
        print(x)
        print("Total runtime: {0:.2f}".format(total_time))
