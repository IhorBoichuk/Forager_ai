from typing import Type, Dict
from services import MyApiClient

"""
handlers.py.

This module provides handlers for various API requests related to hunting pythons in a fictional world.
"""

class Email_Verifier_Handler:
    """
    Email_Verifier_Handler class handles
    the execution of an email verification API request.
    """
    def __init__(self, api_client: Type["MyApiClient"]):
        """
        Initializes the handler with a provided API client.
        
        :param api_client: An instance of the MyApiClient class for making API requests.
        """
        self.api_client = api_client

    def execute(self, email: str) -> Dict:
        """
        Executes the email verification request and returns the JSON response.
        
        :param email: The email address to check
        
        :return: JSON response from the API request.
        """
        endpoint: str = "email-verifier"
        params: Dict[str, str] = {'email': email}
        res = self.api_client.make_request(endpoint, params=params)
        return res.json()

class Domain_Search_Handler:
    """
    Domain_Search_Handler class handles
    the execution of a domain search API request.
    """
    def __init__(self, api_client: Type["MyApiClient"]):
        """
        Initializes the handler with a provided API client.
        
        :param api_client: An instance of the MyApiClient class for making API requests.
        """
        self.api_client = api_client

    def execute(self, domain: str) -> Dict:
        """
        Executes the domain search request and returns the JSON response.
        
        :param domain: The domain name to be searched.
        
        :return: JSON response from the API request.
        """
        endpoint: str = "domain-search"
        params: Dict[str, str] = {'domain': domain}
        res = self.api_client.make_request(endpoint, params=params)
        return res.json()

class Account_Information_Handler:
    """
    Account_Information_Handler class for the execution
    of an API request to retrieve account information.
    """
    def __init__(self, api_client: Type["MyApiClient"]):
        """
        Initializes the handler with a provided API client.
        
        :param api_client: An instance of the MyApiClient
        class for making API requests.
        """
        self.api_client = api_client

    def execute(self) -> Dict:
        """Return respons from hunter.

        Verify the account and return the JSON response.

        :return: A dictionary representing the JSON response

        from the API request.
        """
        endpoint: str = 'account'
        request_params: Dict[str, str] = {'api_key': self.api_client.api_key}
        res = self.api_client.make_request(endpoint, params=request_params)
        return res.json()
