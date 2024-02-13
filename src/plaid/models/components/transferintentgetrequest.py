"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferIntentGetRequest:
    r"""Defines the request schema for `/transfer/intent/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    transfer_intent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_intent_id') }})
    r"""Plaid's unique identifier for a transfer intent object."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

