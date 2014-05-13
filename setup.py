#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='sphinx_rtfd',
    version='0.1.1',
    description='Demonstration of Sphinx and RTFD for PUG',
    long_description=readme + '\n\n' + history,
    author='Rigel Trajano',
    author_email='whichone@gmail.com',
    url='https://github.com//sphinx_rtfd',
    packages=[
        'sphinx_rtfd',
    ],
    package_dir={'sphinx_rtfd':
                 'sphinx_rtfd'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='sphinx_rtfd',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)