#!/usr/bin/env python

from distutils.core import setup

setup(name='array_to_latex',
      version='0.30b',
      description='Return Numpy arrays as formatted LaTeX arrays',
      author='Joseph C. Slater',
      author_email='joseph.c.slater@gmail.com',
      url='https://github.com/josephcslater/array_to_latex/',
      download_url='https://github.com/josephcslater/array_to_latex/archive/0.30b.tar.gz',
      packages=['array_to_latex'],
      long_description = read('README.rst')
      keywords=['latex','array','format']
      )
