"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import plaiderror as components_plaiderror
from ...models.components import transferintentgetresponse as components_transferintentgetresponse
from typing import Optional


@dataclasses.dataclass
class TransferIntentGetResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Error response"""
    transfer_intent_get_response: Optional[components_transferintentgetresponse.TransferIntentGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    

