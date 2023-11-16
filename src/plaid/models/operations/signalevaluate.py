"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import plaiderror as components_plaiderror
from ...models.components import signalevaluateresponse as components_signalevaluateresponse
from typing import Optional


@dataclasses.dataclass
class SignalEvaluateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response."""
    signal_evaluate_response: Optional[components_signalevaluateresponse.SignalEvaluateResponse] = dataclasses.field(default=None)
    r"""OK"""
    

