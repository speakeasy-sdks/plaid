"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import processoridentitymatchresponse as components_processoridentitymatchresponse
from typing import Optional


@dataclasses.dataclass
class ProcessorIdentityMatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    processor_identity_match_response: Optional[components_processoridentitymatchresponse.ProcessorIdentityMatchResponse] = dataclasses.field(default=None)
    r"""OK"""
    

