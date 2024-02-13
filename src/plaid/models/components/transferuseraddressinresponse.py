"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferUserAddressInResponse:
    r"""The address associated with the account holder."""
    UNSET='__SPEAKEASY_UNSET__'
    city: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    r"""Ex. \\"San Francisco\\" """
    country: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""A two-letter country code (e.g., \\"US\\")."""
    postal_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""The postal code (e.g., \\"94103\\")."""
    region: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""The state or province (e.g., \\"CA\\")."""
    street: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street') }})
    r"""The street number and name (i.e., \\"100 Market St.\\")."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

