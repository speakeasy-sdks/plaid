"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import wallettransactiongetresponse as components_wallettransactiongetresponse
from typing import Optional


@dataclasses.dataclass
class WalletTransactionGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    wallet_transaction_get_response: Optional[components_wallettransactiongetresponse.WalletTransactionGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    

