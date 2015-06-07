# README

This provides a library for the uh.cx link shortening service.

[![Build Status](https://travis-ci.org/jeboehm/uhcx-python-lib.svg?branch=master)](https://travis-ci.org/jeboehm/uhcx-python-lib)

## Installation

``` shell
pip3 install uhcx
```

## Usage

``` python
from uhcx import Manager

link = Manager.create('http://www.google.com/')

print(link.url_original)
print(link.url_redirect)
print(link.url_preview)
print(link.qr_redirect)
print(link.qr_preview)
```

## More information

For more information visit http://uh.cx/

Have fun!
