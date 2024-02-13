"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .pay import Pay
from .totalcanonicaldescription import TotalCanonicalDescription
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Total:
    r"""An object representing both the current pay period and year to date amount for a category.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    canonical_description: Optional[TotalCanonicalDescription] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canonical_description'), 'exclude': lambda f: f is Total.UNSET }})
    r"""Commonly used term to describe the line item."""
    current_pay: Optional[Pay] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_pay'), 'exclude': lambda f: f is None }})
    r"""An object representing a monetary amount.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is Total.UNSET }})
    r"""Text of the line item as printed on the paystub."""
    ytd_pay: Optional[Pay] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ytd_pay'), 'exclude': lambda f: f is None }})
    r"""An object representing a monetary amount.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

