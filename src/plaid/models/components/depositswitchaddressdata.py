"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DepositSwitchAddressData:
    r"""The user's address."""
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    r"""The full city name"""
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""The ISO 3166-1 alpha-2 country code"""
    postal_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code') }})
    r"""The postal code"""
    region: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""The region or state
    Example: `\"NC\"`
    """
    street: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street') }})
    r"""The full street address
    Example: `\"564 Main Street, APT 15\"`
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

