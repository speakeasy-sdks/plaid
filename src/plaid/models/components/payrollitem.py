"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .payrollincomeaccountdata import PayrollIncomeAccountData
from .payrollincomeobject import PayrollIncomeObject
from .payrollitemstatus import PayrollItemStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayrollItem:
    r"""An object containing information about the payroll item."""
    accounts: List[PayrollIncomeAccountData] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    institution_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id') }})
    r"""The unique identifier of the institution associated with the Item."""
    institution_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_name') }})
    r"""The name of the institution associated with the Item."""
    item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id') }})
    r"""The `item_id` of the Item associated with this webhook, warning, or error"""
    payroll_income: List[PayrollIncomeObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payroll_income') }})
    status: Optional[PayrollItemStatus] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Details about the status of the payroll item."""
    updated_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the Item was updated."""
    

