#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import threading
import time


class SpinnerWriter(object):
    def __init__(self, type):
        self._spinner = self._spinner_gen(type)

    @staticmethod
    def _spinner_gen(type):
        if type == 'bar':
            while 1:
                yield '|'
                yield '/'
                yield '-'
                yield '\\'

    def print_next_frame(self):
        print('\033[s\033[1K' + next(self._spinner) + '\033[u', end='', file=sys.stderr)


class Spin(threading.Thread):
    def __init__(self, type='bar', duration=.05):
        super(Spin, self).__init__()
        self._type = type
        self._duration = duration
        self._exit = False

    def run(self):
        spinner = SpinnerWriter(self._type)
        while not self._exit:
            spinner.print_next_frame()
            sys.stderr.flush()
            time.sleep(self._duration)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit = True
        return True
