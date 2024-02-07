"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import processortokenwebhookupdateresponse as components_processortokenwebhookupdateresponse
from typing import Optional


@dataclasses.dataclass
class ProcessorTokenWebhookUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    processor_token_webhook_update_response: Optional[components_processortokenwebhookupdateresponse.ProcessorTokenWebhookUpdateResponse] = dataclasses.field(default=None)
    r"""OK"""
    

