"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditbankincomeaccounttype import CreditBankIncomeAccountType
from .depositoryaccountsubtype import DepositoryAccountSubtype
from .owner import Owner
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankIncomeAccount:
    r"""The Item's bank accounts that have the selected data."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Plaid's unique identifier for the account."""
    mask: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mask') }})
    r"""The last 2-4 alphanumeric characters of an account's official account number.
    Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.
    """
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the bank account."""
    official_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('official_name') }})
    r"""The official name of the bank account."""
    owners: List[Owner] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owners') }})
    r"""Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array."""
    subtype: DepositoryAccountSubtype = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtype') }})
    r"""Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository)."""
    type: CreditBankIncomeAccountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The account type. This will always be `depository`."""
    
