"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import creditbankincomerefreshresponse as components_creditbankincomerefreshresponse
from typing import Optional


@dataclasses.dataclass
class CreditBankIncomeRefreshResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    credit_bank_income_refresh_response: Optional[components_creditbankincomerefreshresponse.CreditBankIncomeRefreshResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

