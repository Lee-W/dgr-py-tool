# -*- coding: utf-8 -*-
"""
dgr-py-tool: A tool for Data Garage usage

Usage
-----

Usage is simple::

    import dgr

"""

from setuptools import setup

setup(
    name='dgr',
    version='0.0.1',
    url='https://github.com/DataGarage/dgr-py-tool',
    license='MIT',
    author='chilijung',
    author_email='chilijung@gmail.com',
    description='A tool for Data Garage',
    long_description=__doc__,
    install_requires=[
        'requests'
    ],
    py_modules=['dgr'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)