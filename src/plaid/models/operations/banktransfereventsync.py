"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import banktransfereventsyncresponse as components_banktransfereventsyncresponse
from ...models.components import plaiderror as components_plaiderror
from typing import Optional


@dataclasses.dataclass
class BankTransferEventSyncResponse:
    UNSET='__SPEAKEASY_UNSET__'
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    bank_transfer_event_sync_response: Optional[components_banktransfereventsyncresponse.BankTransferEventSyncResponse] = dataclasses.field(default=None)
    r"""OK"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=UNSET)
    r"""Error response"""
    

