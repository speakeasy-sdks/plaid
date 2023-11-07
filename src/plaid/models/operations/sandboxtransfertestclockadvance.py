"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import plaiderror as components_plaiderror
from ...models.components import sandboxtransfertestclockadvanceresponse as components_sandboxtransfertestclockadvanceresponse
from typing import Optional


@dataclasses.dataclass
class SandboxTransferTestClockAdvanceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    sandbox_transfer_test_clock_advance_response: Optional[components_sandboxtransfertestclockadvanceresponse.SandboxTransferTestClockAdvanceResponse] = dataclasses.field(default=None)
    r"""OK"""
    

