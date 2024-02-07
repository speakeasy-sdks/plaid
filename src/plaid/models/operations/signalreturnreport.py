"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import plaiderror as components_plaiderror
from ...models.components import signalreturnreportresponse as components_signalreturnreportresponse
from typing import Optional


@dataclasses.dataclass
class SignalReturnReportResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response."""
    signal_return_report_response: Optional[components_signalreturnreportresponse.SignalReturnReportResponse] = dataclasses.field(default=None)
    r"""OK"""
    

