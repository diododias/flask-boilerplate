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
    name='flask-boilerplate',
    version='0.0.1',
    description="A Flask clean architecture boilerplate",
    long_description=readme,
    author="Luiz Gustavo Dias",
    author_email='luizgtvgustavo@gmail.com',
    url='',
    packages=[
        'flask-boilerplate',
    ],
    package_dir={'flask-boilerplate':
                 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask-boilerplate',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
