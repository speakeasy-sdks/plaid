"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import paymentprofileremoveresponse as components_paymentprofileremoveresponse
from ...models.components import plaiderror as components_plaiderror
from typing import Optional


@dataclasses.dataclass
class PaymentProfileRemoveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    payment_profile_remove_response: Optional[components_paymentprofileremoveresponse.PaymentProfileRemoveResponse] = dataclasses.field(default=None)
    r"""OK"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    

