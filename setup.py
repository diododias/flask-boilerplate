#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='rentomatic',
    version='0.1.0',
    description="A clean architecture demo project in Python",
    long_description=readme,
    author="Luiz Gustavo Dias",
    author_email='luizgtvgustavo@gmail.com',
    url='',
    packages=[
        'flask_base',
    ],
    package_dir={'flask_base':
                 'app'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_base',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
