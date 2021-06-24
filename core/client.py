# -*- coding: utf-8 -*-
import requests
import allure
import os
import json
from urllib.parse import unquote

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Client:
    def __init__(self, host, **kwargs):
        self.host = host
        self.session = requests.session()

    @allure.step('setp in client.py::Client')
    def post(self, url, payloads=None, **kwargs):
        res = self.session.post(self.host + url, json=payloads, **kwargs)
        allure.attach(json.dumps(payloads, ensure_ascii=False), 'request payloads', allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(self.session.headers.items())), 'request header', allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(res.headers.items())), 'response header', allure.attachment_type.TEXT)
        if res.headers.get('Content-Type').find('application/octet-stream'):
            allure.attach(res.text, 'response data', allure.attachment_type.TEXT)
            try:
                result = res.json()
            except Exception:
                result = {
                    'code': -1,
                    'message': res.text
                }
        else:
            n = unquote(res.headers.get('Content-Disposition').split('\'\'')[1])
            filename = os.path.join(BASE_PATH, 'tmp', n)

            with open(filename, 'wb+') as f:
                f.write(res.content)
            _, filetype = os.path.splitext(filename)
            allure.attach(res.content, filename, attachment_type='application/octet-stream', extension=filetype)
            result = {
                'code': 0,
                'filename': filename
            }

        return result
