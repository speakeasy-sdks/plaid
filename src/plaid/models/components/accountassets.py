"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountbalance import AccountBalance
from .accountsubtype import AccountSubtype
from .accounttype import AccountType
from .assetreporttransaction import AssetReportTransaction
from .historicalbalance import HistoricalBalance
from .owner import Owner
from .ownershiptype import OwnershipType
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from plaid import utils
from typing import Any, Dict, List, Optional

class VerificationStatus(str, Enum):
    r"""The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.

    `pending_automatic_verification`: The Item is pending automatic verification

    `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the micro-deposit.

    `automatically_verified`: The Item has successfully been automatically verified	

    `manually_verified`: The Item has successfully been manually verified

    `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.
    """
    AUTOMATICALLY_VERIFIED = 'automatically_verified'
    PENDING_AUTOMATIC_VERIFICATION = 'pending_automatic_verification'
    PENDING_MANUAL_VERIFICATION = 'pending_manual_verification'
    MANUALLY_VERIFIED = 'manually_verified'
    VERIFICATION_EXPIRED = 'verification_expired'
    VERIFICATION_FAILED = 'verification_failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountAssets:
    r"""A single account at a financial institution."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.

    The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.

    If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the `account_id` is case sensitive.
    """
    balances: AccountBalance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balances') }})
    r"""A set of fields describing the balance for an account. Balance information may be cached unless the balance object was returned by `/accounts/balance/get`."""
    days_available: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_available') }})
    r"""The duration of transaction history available for this Item, typically defined as the time since the date of the earliest transaction in that account."""
    historical_balances: List[HistoricalBalance] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_balances') }})
    r"""Calculated data about the historical balances on the account."""
    mask: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mask') }})
    r"""The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the account, either assigned by the user or by the financial institution itself"""
    official_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('official_name') }})
    r"""The official name of the account as given by the financial institution"""
    owners: List[Owner] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owners') }})
    r"""Data returned by the financial institution about the account owner or owners.For business accounts, the name reported may be either the name of the individual or the name of the business, depending on the institution. Multiple owners on a single account will be represented in the same `owner` object, not in multiple owner objects within the array. In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29)"""
    subtype: Optional[AccountSubtype] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtype') }})
    r"""See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes."""
    transactions: List[AssetReportTransaction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions') }})
    r"""Transaction history associated with the account."""
    type: AccountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""`investment:` Investment account. In API versions 2018-05-22 and earlier, this type is called `brokerage` instead.

    `credit:` Credit card

    `depository:` Depository account

    `loan:` Loan account

    `other:` Non-specified account type

    See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    ownership_type: Optional[OwnershipType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ownership_type') }})
    r"""How an asset is owned.

    `association`: Ownership by a corporation, partnership, or unincorporated association, including for-profit and not-for-profit organizations.
    `individual`: Ownership by an individual.
    `joint`: Joint ownership by multiple parties.
    `trust`: Ownership by a revocable or irrevocable trust.
    """
    persistent_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('persistent_account_id'), 'exclude': lambda f: f is None }})
    r"""A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account across different Items for depository accounts. This is currently an opt-in field and only supported for Chase Items."""
    verification_status: Optional[VerificationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verification_status'), 'exclude': lambda f: f is None }})
    r"""The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.

    `pending_automatic_verification`: The Item is pending automatic verification

    `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the micro-deposit.

    `automatically_verified`: The Item has successfully been automatically verified	

    `manually_verified`: The Item has successfully been manually verified

    `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.
    """
    

