# -*- coding: utf-8 -*-
"""
uh.cx API interface

http://uh.cx/
"""

import unittest
import uhcx


class APITests(unittest.TestCase):
    def testCreateLink(self):
        api = uhcx.API()
        link = api.create('http://www.google.de/')
        self.assertEqual(u'http://www.google.de/', link.get_url_original())


def main():
    unittest.main()


if __name__ == '__main__':
    main()