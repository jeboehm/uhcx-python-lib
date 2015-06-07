"""
Python library for the uh.cx link shortener.

http://uh.cx/

Example!
"""

from uhcx import Manager

link = Manager.create('http://www.google.com/')

print(link.url_original)
print(link.url_redirect)
print(link.url_preview)
print(link.qr_redirect)
print(link.qr_preview)
