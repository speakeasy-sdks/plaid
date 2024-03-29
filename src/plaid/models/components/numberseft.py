"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NumbersEFT:
    r"""Identifying information for transferring money to or from a Canadian bank account via EFT."""
    UNSET='__SPEAKEASY_UNSET__'
    account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""The EFT account number for the account"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The Plaid account ID associated with the account numbers"""
    branch: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch') }})
    r"""The EFT branch number for the account"""
    institution: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution') }})
    r"""The EFT institution number for the account"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

