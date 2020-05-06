# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

"""Setup file for PowerStore SDK"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='PyPowerStore',
      version='1.1.0.0',
      description='Python Library for Dell EMC PowerStore',
      author='Prashant Rakheja',
      author_email='prashant.rakheja@dell.com',
      install_requires=['requests'],
      url='https://github.com/dell',
      packages=['PyPowerStore', 'PyPowerStore.utils'],
      )
