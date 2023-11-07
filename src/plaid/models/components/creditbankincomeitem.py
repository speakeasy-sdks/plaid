"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .creditbankincomeaccount import CreditBankIncomeAccount
from .creditbankincomesource import CreditBankIncomeSource
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankIncomeItem:
    r"""The details and metadata for an end user's Item."""
    bank_income_accounts: Optional[List[CreditBankIncomeAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_income_accounts'), 'exclude': lambda f: f is None }})
    r"""The Item's accounts that have Bank Income data."""
    bank_income_sources: Optional[List[CreditBankIncomeSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_income_sources'), 'exclude': lambda f: f is None }})
    r"""The income sources for this Item. Each entry in the array is a single income source."""
    institution_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier of the institution associated with the Item."""
    institution_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_name'), 'exclude': lambda f: f is None }})
    r"""The name of the institution associated with the Item."""
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the Item."""
    last_updated_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_updated_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The time when this Item's data was last retrieved from the financial institution."""
    

