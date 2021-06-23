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
        allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        try:
            return res.json()
        except Exception as e:
            return {'code': -1,
                    'error': str(e),
                    'data': res.text
                    }

    @allure.step('setp in client.py::Client')
    def post_file(self, url, payloads=None, **kwargs):
        res = self.session.post(self.host + url, json=payloads, **kwargs)
        allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        try:
            n = unquote(res.headers.get('Content-Disposition').split('\'\'')[1])
            filename = os.path.join(BASE_PATH, 'tmp', n)

            with open(filename, 'wb+') as f:
                f.write(res.content)
            _, filetype = os.path.splitext(filename)
            allure.attach(res.content, filename, attachment_type='application/octet-stream', extension=filetype)
            r = {
                'code': 0,
                'filename': filename
            }
            allure.attach(json.dumps(r), 'Response', attachment_type=allure.attachment_type.TEXT)
        except Exception:
            r = res.json()
            allure.attach(res.text, 'Response', attachment_type=allure.attachment_type.TEXT)
        return r
