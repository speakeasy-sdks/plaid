"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from plaid.models import components


SERVERS = [
    'https://production.plaid.com',
    # Production
    'https://development.plaid.com',
    # Development
    'https://sandbox.plaid.com',
    # Sandbox
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '2020-09-14_1.421.0'
    sdk_version: str = '0.6.0'
    gen_version: str = '2.250.12'
    user_agent: str = 'speakeasy-sdk/python 0.6.0 2.250.12 2020-09-14_1.421.0 plaid'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
