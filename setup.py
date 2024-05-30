# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Dell Technologies

"""Setup file for PowerStore SDK"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='PyPowerStore',
      version='3.3.0.0',
      description='Python Library for Dell PowerStore',
      author='Ansible Team at Dell',
      author_email='ansible.team@dell.com',
      install_requires=[
        'urllib3>=1.26.7',
        'requests>=2.23.0'
      ],
      license_files = ('LICENSE',),
      classifiers=['License :: OSI Approved :: Apache Software License'],
      url='https://github.com/dell/python-powerstore',
      packages=['PyPowerStore', 'PyPowerStore.utils', 'PyPowerStore.objects'],
      )
