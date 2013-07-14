# -*- coding: utf-8 -*-
"""
uh.cx API interface

http://uh.cx/
"""

import urllib2
import json
import exception


class API:
    _create_address = 'http://uh.cx/api/create/json'

    def __init__(self):
        pass

    def create(self, url):
        """

        :rtype : Link
        """
        data = {
            'url': url
        }

        response = self._decode_response(self._get_response(data))
        link = self._factory_link(response)
        return link

    def _request_factory(self):
        request = urllib2.Request(self._create_address)
        request.add_header('Content-type', 'application/json')
        return request

    def _get_response(self, data):
        try:
            response = urllib2.urlopen(self._request_factory(), json.dumps(data))
        except urllib2.URLError:
            raise exception.CouldNotConnectException()

        if response.msg != 'OK' or response.code != 200:
            raise exception.CouldNotConnectException()

        return response.readline()

    def _decode_response(self, response):
        try:
            return_value = json.loads(response, 'utf-8')
            return return_value
        except ValueError:
            raise exception.CouldNotDecodeJsonException()

    def _factory_link(self, response):
        link = Link(response)
        return link


class Link():
    __response = {}
    __keys = ['QrDirect', 'QrPreview', 'UrlDirect', 'UrlPreview', 'UrlOriginal']

    def __init__(self, response):
        self.__response = response

        for key in self.__keys:
            if key not in self.__response:
                raise exception.InvalidResponseException()

    def get_qr_direct(self):
        return self.__response['QrDirect']

    def get_qr_preview(self):
        return self.__response['QrPreview']

    def get_url_direct(self):
        return self.__response['UrlDirect']

    def get_url_preview(self):
        return self.__response['UrlPreview']

    def get_url_original(self):
        return self.__response['UrlOriginal']
