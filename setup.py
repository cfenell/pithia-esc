#! /usr/bin/env python3

from setuptools import setup
setup(
    name='validate',
    description='XML validation with Python XMLSchema',
    author='Carl-Fredrik Enell',
    author_email='carl-fredrik.enell@eiscat.se',
    install_requires=['xmlschema'],
    scripts=['validate.py']
)
