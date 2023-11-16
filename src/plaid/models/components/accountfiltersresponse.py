"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfilter import CreditFilter
from .depositoryfilter import DepositoryFilter
from .investmentfilter import InvestmentFilter
from .loanfilter import LoanFilter
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountFiltersResponse:
    r"""The `account_filters` specified in the original call to `/link/token/create`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    credit: Optional[CreditFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `credit`-type accounts"""
    depository: Optional[DepositoryFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('depository'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `depository`-type accounts"""
    investment: Optional[InvestmentFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('investment'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `investment`-type accounts (or `brokerage`-type accounts for API versions 2018-05-22 and earlier)."""
    loan: Optional[LoanFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan'), 'exclude': lambda f: f is None }})
    r"""A filter to apply to `loan`-type accounts"""
    

