#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


__author__ = 'Shintaro Morikawa <sntr92@gmail.com>'
__version__ = '0.1'

setup(name='spinner',
      version=__version__,
      description='Show spinner animation during processing',
      author=__author__,
      author_email='sntr92@gmail.com',
      license = "MIT License",
      url='https://github.com/morishin/spinner',
      packages=['spinner'],
      scripts=['scripts/spin'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7'
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4'
      ])

