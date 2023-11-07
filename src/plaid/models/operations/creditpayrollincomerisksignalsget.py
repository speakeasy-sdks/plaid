"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import creditpayrollincomerisksignalsgetresponse as components_creditpayrollincomerisksignalsgetresponse
from typing import Optional


@dataclasses.dataclass
class CreditPayrollIncomeRiskSignalsGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    credit_payroll_income_risk_signals_get_response: Optional[components_creditpayrollincomerisksignalsgetresponse.CreditPayrollIncomeRiskSignalsGetResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

