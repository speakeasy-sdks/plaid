"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountbase import AccountBase
from .holding import Holding
from .investmentsauthgetnumbers import InvestmentsAuthGetNumbers
from .investmentsauthowner import InvestmentsAuthOwner
from .item import Item
from .security import Security
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvestmentsAuthGetResponse:
    r"""InvestmentsAuthGetResponse defines the response schema for `/investments/auth/get`"""
    UNSET='__SPEAKEASY_UNSET__'
    accounts: List[AccountBase] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    r"""The accounts for which data is being retrieved"""
    holdings: List[Holding] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holdings') }})
    r"""The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field."""
    item: Item = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item') }})
    r"""Metadata about the Item."""
    numbers: InvestmentsAuthGetNumbers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numbers') }})
    r"""Identifying information for transferring holdings to an investments account."""
    owners: List[InvestmentsAuthOwner] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owners') }})
    r"""Information about the account owners for the accounts associated with the Item."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    securities: List[Security] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securities') }})
    r"""Objects describing the securities held in the accounts associated with the Item."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

