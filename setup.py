#!/usr/bin/env python

from distutils.core import setup
import os
#from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='array_to_latex',
      version='0.32b',
      description='Return Numpy arrays as formatted LaTeX arrays. pip install --user array_to_latex',
      author='Joseph C. Slater',
      author_email='joseph.c.slater@gmail.com',
      url='https://github.com/josephcslater/array_to_latex/',
      download_url='https://github.com/josephcslater/array_to_latex/archive/0.32b.tar.gz',
      packages=['array_to_latex'],
      long_description = read('README.md'),
      keywords=['latex','array','format','numpy'],
      install_requires=[
      'numpy',
      'clipboard'
      ]
      )
