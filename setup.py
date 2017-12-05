#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='campaign-finance',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'alembic==0.9.2',
        'click==6.7',
        'Flask==0.12.2',
        'Flask-Admin==1.5.0',
        'Flask-SQLAlchemy==2.3.2',
        'gunicorn==19.7.1',
        'psycopg2==2.7.3',
        'SQLAlchemy==1.1.10'
    ]
)
