"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditsessionbankincomestatus import CreditSessionBankIncomeStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditSessionBankIncomeResult:
    r"""The details of a bank income verification in Link"""
    institution_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid Institution ID associated with the Item."""
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive."""
    status: Optional[CreditSessionBankIncomeStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the Bank Income Link session.

    `APPROVED`: User has approved and verified their income

    `NO_DEPOSITS_FOUND`: We attempted, but were unable to find any income in the connected account.

    `USER_REPORTED_NO_INCOME`: The user explicitly indicated that they don't receive income in the connected account.

    `STARTED`: The user began the bank income portion of the link flow.

    `INTERNAL_ERROR`: The user encountered an internal error.
    """
    
