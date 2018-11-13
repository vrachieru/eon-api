#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()

setup(
    name='eon',
    version='0.1.0',
    description='E.ON Myline API wrapper',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Victor Rachieru',
    python_requires='>=3.0.0',
    url='https://github.com/vrachieru/eon-api',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',        
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License'
    ]
)