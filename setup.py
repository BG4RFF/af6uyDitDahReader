# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ditDahReader',
    version='0.1.0',
    description='AF6UY Dit Dah (IRC) Reader',
    long_description=readme,
    author='Richard J. Tobias (af6uy)',
    author_email='dspmathguru@gmail.com',
    url='https://github.com/dspmathgur/af6uyDitDayReder',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
