"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import plaiderror as components_plaiderror
from ...models.components import transactionsrefreshresponse as components_transactionsrefreshresponse
from typing import Optional


@dataclasses.dataclass
class TransactionsRefreshResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Error response"""
    transactions_refresh_response: Optional[components_transactionsrefreshresponse.TransactionsRefreshResponse] = dataclasses.field(default=None)
    r"""OK"""
    

