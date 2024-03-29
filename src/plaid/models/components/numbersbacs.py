"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NumbersBACS:
    r"""Identifying information for transferring money to or from a UK bank account via BACS."""
    UNSET='__SPEAKEASY_UNSET__'
    account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""The BACS account number for the account"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Plaid account ID associated with the account numbers"""
    sort_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort_code') }})
    r"""The BACS sort code for the account"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

