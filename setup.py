from __future__ import print_function
from setuptools import setup

setup(
    name='Skeleton',
    version='0.1',
    url='url',
    license='MIT',
    author='Scott Olesen',
    tests_require=['pytest'],
    install_requires=[
        'requests'
        ],
    author_email='jeff@jeffknupp.com',
    description='Automated REST APIs for legacy (existing) databases',
    long_description='long desc',
    packages=['skeleton'],
    scripts=['scripts/run_skeleton.py']
)
