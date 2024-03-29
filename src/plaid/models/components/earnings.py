"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .earningsbreakdown import EarningsBreakdown
from .earningstotal import EarningsTotal
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Earnings:
    r"""An object representing both a breakdown of earnings on a paystub and the total earnings."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    breakdown: Optional[List[EarningsBreakdown]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breakdown'), 'exclude': lambda f: f is None }})
    subtotals: Optional[List[EarningsTotal]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotals'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    total: Optional[EarningsTotal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total'), 'exclude': lambda f: f is None }})
    r"""An object representing both the current pay period and year to date amount for an earning category."""
    totals: Optional[List[EarningsTotal]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totals'), 'exclude': lambda f: f is None }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    

