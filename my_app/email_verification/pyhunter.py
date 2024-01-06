""" 
pyhunter.py

Description: This script provides functionality 
related to hunting pythons in a fictional world.
"""

import requests

from email_verification.exceptions import HunterApiError


class PyHunter:
    """
    PythonHunter class for hunting pythons in a fictional world.
    """

    def __init__(self, api_key):
        """
        Initialize a PythonHunter instance.

        :param api_key: Your secret API key.You can generate in your dashboard.
        
        """
        self.api_key = api_key
        self.base_params = {'api_key': api_key}
        self.base_endpoint = 'https://api.hunter.io/v2/{}'

    def _query_hunter(self, endpoint, params, request_type='get',
                      payload=None, headers=None, raw=False):

        request_kwargs = dict(params=params, json=payload, headers=headers)
        res = getattr(requests, request_type)(endpoint, **request_kwargs)
        res.raise_for_status()
        if raw:
            return res

        try:
            data = res.json()['data']
        except KeyError:
            raise HunterApiError(res.json())

        return data


    def email_verifier(self, email, raw=False):
        """
        Verify the deliverability of a given email address.

        :param email: The email address to check.

        :param raw: Gives back the entire response instead of just the 'data'.

        :return: Full payload of the query as a dict.
        """
        params = {'email': email, 'api_key': self.api_key}

        endpoint = self.base_endpoint.format('email-verifier')

        return self._query_hunter(endpoint, params, raw=raw)
