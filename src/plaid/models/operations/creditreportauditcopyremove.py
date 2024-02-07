"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import creditauditcopytokenremoveresponse as components_creditauditcopytokenremoveresponse
from typing import Optional


@dataclasses.dataclass
class CreditReportAuditCopyRemoveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    credit_audit_copy_token_remove_response: Optional[components_creditauditcopytokenremoveresponse.CreditAuditCopyTokenRemoveResponse] = dataclasses.field(default=None)
    r"""OK"""
    

