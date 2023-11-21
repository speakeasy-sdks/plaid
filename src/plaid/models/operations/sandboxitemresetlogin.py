"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import sandboxitemresetloginresponse as components_sandboxitemresetloginresponse
from typing import Optional


@dataclasses.dataclass
class SandboxItemResetLoginResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    sandbox_item_reset_login_response: Optional[components_sandboxitemresetloginresponse.SandboxItemResetLoginResponse] = dataclasses.field(default=None)
    r"""OK"""
    
