"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountbalance import AccountBalance
from .accountsubtype import AccountSubtype
from .accounttype import AccountType
from .addressmatchscore import AddressMatchScore
from .emailaddressmatchscore import EmailAddressMatchScore
from .namematchscore import NameMatchScore
from .phonenumbermatchscore import PhoneNumberMatchScore
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from plaid import utils
from typing import Any, Dict, Optional

class AccountIdentityMatchScoreVerificationStatus(str, Enum):
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
class AccountIdentityMatchScore:
    r"""Identity match scores for an account"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.

    The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.

    If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the `account_id` is case sensitive.
    """
    balances: AccountBalance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balances') }})
    r"""A set of fields describing the balance for an account. Balance information may be cached unless the balance object was returned by `/accounts/balance/get`."""
    mask: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mask') }})
    r"""The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the account, either assigned by the user or by the financial institution itself"""
    official_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('official_name') }})
    r"""The official name of the account as given by the financial institution"""
    subtype: Optional[AccountSubtype] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtype') }})
    r"""See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes."""
    type: AccountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""`investment:` Investment account. In API versions 2018-05-22 and earlier, this type is called `brokerage` instead.

    `credit:` Credit card

    `depository:` Depository account

    `loan:` Loan account

    `other:` Non-specified account type

    See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    address: Optional[AddressMatchScore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Score found by matching address provided by the API with the address on the account at the financial institution. The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled."""
    email_address: Optional[EmailAddressMatchScore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address') }})
    r"""Score found by matching email provided by the API with the email on the account at the financial institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled."""
    legal_name: Optional[NameMatchScore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_name') }})
    r"""Score found by matching name provided by the API with the name on the account at the financial institution. If the account contains multiple owners, the maximum match score is filled."""
    persistent_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('persistent_account_id'), 'exclude': lambda f: f is None }})
    r"""A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account across different Items for depository accounts. This is currently an opt-in field and only supported for Chase Items."""
    phone_number: Optional[PhoneNumberMatchScore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    r"""Score found by matching phone number provided by the API with the phone number on the account at the financial institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled."""
    verification_status: Optional[AccountIdentityMatchScoreVerificationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verification_status'), 'exclude': lambda f: f is None }})
    r"""The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.

    `pending_automatic_verification`: The Item is pending automatic verification

    `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the micro-deposit.

    `automatically_verified`: The Item has successfully been automatically verified	

    `manually_verified`: The Item has successfully been manually verified

    `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.
    """
    

