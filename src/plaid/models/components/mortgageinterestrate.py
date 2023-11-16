"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MortgageInterestRate:
    r"""Object containing metadata about the interest rate for the mortgage."""
    percentage: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('percentage') }})
    r"""Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan."""
    type: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of interest charged (fixed or variable)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

