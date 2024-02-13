"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountidentity import AccountIdentity
from .item import Item
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IdentityGetResponse:
    r"""IdentityGetResponse defines the response schema for `/identity/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    accounts: List[AccountIdentity] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    r"""The accounts for which Identity data has been requested"""
    item: Item = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item') }})
    r"""Metadata about the Item."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

