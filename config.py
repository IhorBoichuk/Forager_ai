"""
config.py.

This module provides configuration settings for the application.

It includes the base URL for the Hunter.io API and retrieves the API key
from the environment variable 'API_KEY'.
"""

import os
from typing import Optional

BASE_URL: str = 'https://api.hunter.io/v2'
API_KEY: Optional[str] = os.environ.get('API_KEY')
MAX_DOMAIN_LENGTH: int = 200
