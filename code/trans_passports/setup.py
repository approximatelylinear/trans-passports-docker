#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put additional package requirements here
]

test_requirements = [
    # TODO: put additional package test requirements here
]

setup(
    name='trans_passports',
    version='0.1.0',
    description="Dockerization of the trans-passports codebase",
    long_description=readme + '\n\n' + history,
    author="MJ Berends",
    author_email='mjr.berends@gmail.com',
    url='https://github.com/approximatelylinear/trans_passports',
    packages=[
        'trans_passports',
    ],
    package_dir={'trans_passports':
                 'trans_passports'},
    entry_points={
        'console_scripts': [
            'trans_passports=trans_passports.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='trans_passports',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
