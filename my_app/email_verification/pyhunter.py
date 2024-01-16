"""
pyhunter.py.

Description: This script provides functionality
related to hunting pythons in a fictional world.
"""

from typing import Any, Dict, Union

import requests

from email_verification.exceptions import HunterApiError


class PyHunter:
    """PythonHunter class for hunting pythons in a fictional world."""

    def __init__(self, api_key: str) -> None:
        """
        Initialize a PythonHunter instance.

        :param api_key: Your secret API key.You can generate in your dashboard.
        """
        self.api_key = api_key
        self.base_params: Dict[str, str] = {'api_key': api_key}
        self.base_endpoint: str = 'https://api.hunter.io/v2/email_verifier'

    def email_verifier(
        self, email: str, raw: bool = False,
        ) -> Union[Dict[str, Any], requests.Response]:
        """
        Verify the deliverability of a given email address.

        :param email: The email address to check.

        :param raw: Gives back the entire response instead of just the 'data'.

        :return: Full payload of the query as a dict.
        """
        request_params: Dict[str, str] = {
            'email': email,
            'api_key': self.api_key,
        }

        endpoint: str = self.base_endpoint.format('email-verifier')

        return self._query_hunter(endpoint, params=request_params, raw=raw)

    def _query_hunter(
        self,
        endpoint: str,
        request_params: Dict[str, str],
        request_type: str = 'get',
        raw: bool = False,
    ) -> Union[Dict[str, Any], requests.Response]:

        request_params = Dict[str, str]
        request_kwargs: Dict[str, Union[request_params, None]] = {
            'params': request_params,
            'json': None,
            'headers': None,
        }

        res: requests.Response = getattr(
            requests, request_type,
        )(endpoint, **request_kwargs)
        res.raise_for_status()
        if raw:
            return res

        try:
            result_data: Dict[str, Any] = res.json()['data']
        except KeyError:
            raise HunterApiError(res.json())

        return result_data
