# -*- coding: utf-8 -*-
"""
uh.cx API interface

http://uh.cx/
"""

from distutils.core import setup

setup(
    name='uhcx',
    version='0.1.0',
    author='J. Boehm',
    author_email='jb@uh.cx',
    packages=['uhcx', 'uhcx.test'],
    url='http://uh.cx/page/api',
    license='LICENSE.txt',
    description='Provide an api for uh.cx link shortening service.',
    long_description=open('README.md').read()
)