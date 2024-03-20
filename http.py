"""
  Create By Jared on 
"""
__author__ = "Jared"

from urllib import request
import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)
        if return_json:
            return r.json()
        else:
            return r.text
        pass
