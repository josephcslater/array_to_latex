#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='array_to_latex',
      version='0.36',
      description='Return Numpy arrays as formatted LaTeX arrays.',
      author='Joseph C. Slater',
      author_email='joseph.c.slater@gmail.com',
      url='https://github.com/josephcslater/array_to_latex/',
      download_url='https://github.com/josephcslater/array_to_latex/archive/0.36.tar.gz',
      packages=['array_to_latex'],
      long_description = read('README.rst'),
      keywords=['latex','array','format','numpy','scipy'],
      install_requires=['numpy','clipboard'],
      classifiers = ['Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: MIT License',
                    'Environment :: Console',
                    'Intended Audience :: End Users/Desktop',
                    'Intended Audience :: Education',
                    'Intended Audience :: Science/Research',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3.4',
                    'Programming Language :: Python :: 3.5',
                    'Programming Language :: Python :: 3.6',
                    'Topic :: Scientific/Engineering',
                    'Topic :: Text Processing :: Markup :: LaTeX',
                    'Operating System :: Microsoft :: Windows',
                    'Operating System :: POSIX',
                    'Operating System :: Unix',
                    'Operating System :: MacOS',
                    'Topic :: Utilities']
      )

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
