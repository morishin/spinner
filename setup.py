#!/usr/bin/env python
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup


__author__ = 'Shintaro Morikawa <sntr92@gmail.com>'
__version__ = '0.2'

requires = []

if sys.version_info < (3, 4):
    requires.append('enum34==1.0.4')

setup(name='processing-spinner',
      version=__version__,
      description='Show spinner animation during processing',
      author=__author__,
      author_email='sntr92@gmail.com',
      license = "MIT License",
      url='https://github.com/morishin/spinner',
      packages=['spinner'],
      install_requires=requires,
      scripts=['scripts/spin'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
