#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import threading
import time
from enum import Enum


class SpinnerType(Enum):
    bar = 1
    shobon = 2
    dot = 3
    regiment = 4
    stripe = 5


class SpinnerWriter(object):
    def __init__(self, type):
        self._spinner = self._spinner_gen(type)

    @staticmethod
    def _spinner_gen(type):
        if type == SpinnerType.bar:
            while 1:
                yield '|'
                yield '/'
                yield '-'
                yield '\\'
        elif type == SpinnerType.shobon:
            while 1:
                yield '(´･ω･`)'
                yield '( ´･ω･)'
                yield '(  ´･ω)'
                yield '(   ´･)'
                yield '(    ´)'
                yield '(`    )'
                yield '(･`   )'
                yield '(ω･`  )'
                yield '(･ω･` )'
        elif type == SpinnerType.dot:
            while 1:
                yield ' ----'
                yield '- ---'
                yield '-- --'
                yield '--- -'
                yield '---- '
        elif type == SpinnerType.regiment:
            while 1:
                yield ' ////'
                yield '/ ///'
                yield '// //'
                yield '/// /'
                yield '//// '
        elif type == SpinnerType.stripe:
            while 1:
                yield ' ||||'
                yield '| |||'
                yield '|| ||'
                yield '||| |'
                yield '|||| '

    def print_next_frame(self):
        print('\033[s\033[1K' + next(self._spinner) + '\033[0K\033[u', end='', file=sys.stderr)


class Spin(threading.Thread):
    def __init__(self, type=SpinnerType.bar, duration=.05):
        """Spin Constructor

        Keyword arguments:
        type -- the type of animation object (default SpinnerType.bar)
        duration -- the frame duration (default .05)
        """
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
