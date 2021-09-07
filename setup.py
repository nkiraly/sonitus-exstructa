#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command


def _get_file_lines(path):
    # Gets a list of lines from a file
    with open(path) as handle:
        lines = handle.read().splitlines()
    return lines


# Package meta data
NAME = 'sonitus_exstructa'
DESCRIPTION = 'Structured Logging Log Generator'
URL = 'https://github.com/nkiraly/sonitus-exstructa'
EMAIL = 'kiraly.nicholas@gmail.com'
AUTHOR = 'Nicholas Kiraly'
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '0.0.1'

INSTALL_REQUIREMENTS_PATH = "./requirements.txt"
REQUIRED = _get_file_lines(INSTALL_REQUIREMENTS_PATH)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        'console_scripts': ['sonitus-exstructa=sonitus_exstructa.cli:main'],
    },
    install_requires=REQUIRED,
)
