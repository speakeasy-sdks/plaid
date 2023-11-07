"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditRelayRefreshResponse:
    r"""CreditRelayRefreshResponse defines the response schema for `/credit/relay/refresh`"""
    relay_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relay_token') }})
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    asset_report_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('asset_report_id'), 'exclude': lambda f: f is None }})
    r"""A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""
    

