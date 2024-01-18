from typing import Optional, Dict, Any
import requests

class MyApiClient:
    """
    MyApiClient class provides methods for making HTTP requests to a specified API.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes an instance of MyApiClient.

        :param base_url: The base URL of the API.
        :param api_key: The API key for authentication.
        """
        self.base_url: str = base_url
        self.api_key: str = api_key

    def make_request(self, endpoint: str, method: str = 'GET', params: Optional[Dict[str, Any]] = None,
                      data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Makes an HTTP request to the specified endpoint.

        :param endpoint: The endpoint to make the request to.
        :param method: The HTTP method (default is 'GET').
        :param params: Optional parameters to include in the request.
        :param data: Optional data to include in the request.

        :return: requests.Response object containing the HTTP response.
        """
        url: str = f"{self.base_url}/{endpoint}"
        
        # Ensure params is a dictionary to prevent potential issues
        params = params or {}
        
        # Add API key to parameters
        params['api_key'] = self.api_key

        # Make the request using getattr and lower to handle various HTTP methods
        res: requests.Response = getattr(requests, method.lower())(url, params=params, data=data)

        # Raise an exception for HTTP errors
        res.raise_for_status()

        return res
