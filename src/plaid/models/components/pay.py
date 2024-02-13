"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Pay:
    r"""An object representing a monetary amount.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    amount: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is Pay.UNSET }})
    r"""A numerical amount of a specific currency."""
    currency: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is Pay.UNSET }})
    r"""Currency code, e.g. USD"""
    

