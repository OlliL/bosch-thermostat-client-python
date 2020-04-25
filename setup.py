#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

with open("bosch_thermostat_client/version.py") as f:
    exec(f.read())


REQUIRES = [
    'pyaes>=1.6.1',
    'aiohttp',
    'aioxmpp',
    "click>=7"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bosch-thermostat-client',
    version=__version__,  # type: ignore # noqa: F821,
    description='Python API for talking to Bosch™ Heating gateway using HTTP or XMPP',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ludovic Laurent, Pawel Szafer',
    author_email='ludovic.laurent@gmail.com, pszafer@gmail.com',
    url='https://github.com/bosch-thermostat/bosch-thermostat-client-python',
    download_url='https://github.com/bosch-thermostat/bosch-thermostat-client-python/archive/{}.zip'.format(__version__),
    packages=["bosch_thermostat_client"],
    install_requires=REQUIRES,
    include_package_data=True,
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Other/Nonlisted Topic',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    entry_points={
        "console_scripts": [
            "bosch_scan=bosch_thermostat_client.bosch_rawscan_cli:cli",
            "bosch_examples=bosch_thermostat_client.bosch_examples:cli"
        ]
    }
)