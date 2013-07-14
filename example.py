# -*- coding: utf-8 -*-
"""
uh.cx API interface

http://uh.cx/


Example!
"""

import uhcx

api = uhcx.API()
link = api.create('http://www.google.com/')

print link.get_url_original()
print link.get_url_direct()
print link.get_url_preview()
print link.get_qr_direct()
print link.get_qr_preview()


