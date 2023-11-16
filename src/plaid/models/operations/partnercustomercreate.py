"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import partnercustomercreateresponse as components_partnercustomercreateresponse
from ...models.components import plaiderror as components_plaiderror
from typing import Optional


@dataclasses.dataclass
class PartnerCustomerCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    partner_customer_create_response: Optional[components_partnercustomercreateresponse.PartnerCustomerCreateResponse] = dataclasses.field(default=None)
    r"""OK"""
    plaid_error: Optional[components_plaiderror.PlaidError] = dataclasses.field(default=None)
    r"""Error response"""
    

