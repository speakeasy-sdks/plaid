"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditbankstatementuploadaccountowner import CreditBankStatementUploadAccountOwner
from .creditbankstatementuploadbankaccountperiod import CreditBankStatementUploadBankAccountPeriod
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankStatementUploadBankAccount:
    r"""An object containing data about a user's bank account related to an uploaded bank statement."""
    account_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The unique id of the bank account"""
    account_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""The bank account number."""
    account_type: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_type') }})
    r"""The type of the bank account."""
    bank_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_name') }})
    r"""The name of the bank institution."""
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the bank account"""
    owner: CreditBankStatementUploadAccountOwner = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner') }})
    r"""An object containing data about the owner of the bank account for the uploaded bank statement."""
    periods: List[CreditBankStatementUploadBankAccountPeriod] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('periods') }})
    r"""An array of period objects, containing more data on the overall period of the statement."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

