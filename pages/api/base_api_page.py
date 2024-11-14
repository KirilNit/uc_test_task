import os

import requests


class BaseAPIPage:

    def __init__(self, headers=None):
        if headers:
            assert hasattr(headers, 'x-api-key'), 'x-api-key header must be set in child class` object'
        self.headers = headers or {'x-api-key': os.getenv("API_KEY")}

    def get(self, url, params=None, headers=None):
        resp = requests.get(url, params=params, headers={**self.headers, **(headers or {})})
        if resp.status_code != 200:
            raise Exception('Status code is not 200(OK)')
        return resp

    def post(self, url, data=None, json=None, headers=None):
        resp = requests.post(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        if resp.status_code != 200:
            raise Exception('Status code is not 200(OK)')
        return resp

    def put(self, url, data=None, json=None, headers=None):
        resp = requests.put(url, data=data, json=json, headers={**self.headers, **(headers or {})})
        if resp.status_code != 200:
            raise Exception('Status code is not 200(OK)')
        return resp

    def delete(self, url, headers=None):
        resp = requests.delete(url, headers={**self.headers, **(headers or {})})
        if resp.status_code != 200:
            raise Exception('Status code is not 200(OK)')
        return resp
