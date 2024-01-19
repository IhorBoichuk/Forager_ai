"""
services.py.

This module provides services.
"""
from typing import Any, Dict, Optional

import requests


class MyApiClient:
    """MyApiClient class provides methods for making HTTP requests to API."""

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize an instance of MyApiClient.

        Parameters:
            base_url: The base URL of the API.
            api_key: The API key for authentication.
        """
        self.base_url: str = base_url
        self.api_key: str = api_key

    def make_request(
        self,
        endpoint: str,
        method: str = 'GET',
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Make an HTTP request to the specified endpoint.

        Parameters:
            endpoint: The endpoint to make the request to.
            method: The HTTP method (default is 'GET').
            params: Optional parameters to include in the request.
            data: Optional data to include in the request.

        Returns:
            requests.Response object containing the HTTP response.
        """
        url: str = f'{self.base_url}/{endpoint}'
        params = params or {}
        params['api_key'] = self.api_key

        res: requests.Response = getattr(
            requests,
            method.lower(),
            )(url, params=params, data=data)

        res.raise_for_status()

        return res
