"""
handlers.py.

This module provides handlers for various API requests
related to hunting pythons in a fictional world.
"""

from typing import Dict, Type

from services import MyApiClient


class EmailVerifierHandler:
    """Email_Verifier_Handler class handles email verification API request."""

    def __init__(self, api_client: Type['MyApiClient']):
        """
        Initialize the handler with a provided API client.

        Parameters:
            api_client: An instance of the MyApiClient class for API requests.
        """
        self.api_client = api_client

    def execute(self, email: str) -> Dict:
        """Return respons from hunter.

        Make the email verification request.

        Parameters:
            email: The email address to check

        Returns:
            JSON response from the API request.
        """
        endpoint: str = 'email-verifier'
        request_params: Dict[str, str] = {'email': email}
        res = self.api_client.make_request(endpoint, params=request_params)
        return res.json()


class DomainSearchHandler:
    """Domain_Search_Handler class handles a domain search API request."""

    def __init__(self, api_client: Type['MyApiClient']):
        """
        Initialize the handler with a provided API client.

        Parameters:
            api_client: An instance of the MyApiClient class for API requests.
        """
        self.api_client = api_client

    def execute(self, domain: str) -> Dict:
        """Return respons from hunter.

        Make the domain search request.

        Parameters:
             domain: The domain name to be searched.

        Returns:
            JSON response from the API request.
        """
        endpoint: str = 'domain-search'
        request_params: Dict[str, str] = {'domain': domain}
        res = self.api_client.make_request(endpoint, params=request_params)
        return res.json()


class AccountInformationHandler:
    """Account_Information_Handler class.

    Account_Information_Handler class for the execution
    of an API request to retrieve account information.
    """

    def __init__(self, api_client: Type['MyApiClient']):
        """
         Initialize the handler with a provided API client.

        Parameters:
            api_client: An instance of the MyApiClient

            class for making API requests.
        """
        self.api_client = api_client

    def execute(self) -> Dict:
        """Return respons from hunter.

        Verify the account and return the JSON response.

        Returns:
            A dictionary representing the JSON response
            from the API request.
        """
        endpoint: str = 'account'
        request_params: Dict[str, str] = {'api_key': self.api_client.api_key}
        res = self.api_client.make_request(endpoint, params=request_params)
        return res.json()
