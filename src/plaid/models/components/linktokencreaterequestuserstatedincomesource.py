"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .userstatedincomesourcecategory import UserStatedIncomeSourceCategory
from .userstatedincomesourcefrequency import UserStatedIncomeSourceFrequency
from .userstatedincomesourcepaytype import UserStatedIncomeSourcePayType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenCreateRequestUserStatedIncomeSource:
    r"""Specifies user stated income sources for the Income product"""
    category: Optional[UserStatedIncomeSourceCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category'), 'exclude': lambda f: f is None }})
    r"""The income category for a specified income source"""
    employer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employer'), 'exclude': lambda f: f is None }})
    r"""The employer corresponding to an income source specified by the user"""
    pay_annual: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_annual'), 'exclude': lambda f: f is None }})
    r"""The income amount paid annually for a specified income source"""
    pay_frequency: Optional[UserStatedIncomeSourceFrequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_frequency'), 'exclude': lambda f: f is None }})
    r"""The pay frequency of a specified income source"""
    pay_per_cycle: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_per_cycle'), 'exclude': lambda f: f is None }})
    r"""The income amount paid per cycle for a specified income source"""
    pay_type: Optional[UserStatedIncomeSourcePayType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_type'), 'exclude': lambda f: f is None }})
    r"""The pay type - `GROSS`, `NET`, or `UNKNOWN` for a specified income source"""
    
