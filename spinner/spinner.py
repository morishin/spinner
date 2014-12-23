#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import threading
import time


class SpinnerWriter:
    def __init__(self):
        self._spinner = self._spinner_gen()

    @staticmethod
    def _spinner_gen():
        while 1:
            yield '|'
            yield '/'
            yield '-'
            yield '\\'

    def print_next_frame(self):
        print(next(self._spinner) + '\033[1D', end='', file=sys.stderr)


class Spin(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._exit = False

    def run(self):
        spinner = SpinnerWriter()
        while not self._exit:
            spinner.print_next_frame()
            sys.stderr.flush()
            time.sleep(.05)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit = True
        return True 
