"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NumbersACATS:
    r"""Identifying information for transferring holdings to an investments account via ACATS."""
    account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""The full account number for the account"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Plaid account ID associated with the account numbers"""
    dtc_numbers: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dtc_numbers') }})
    r"""Identifiers for the clearinghouses that are assocciated with the account in order of relevance. This array will be empty if we can't provide any account level data. Institution level data can be retrieved from the institutions/get endpoints."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

