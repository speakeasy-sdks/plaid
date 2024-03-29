"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .pay import Pay
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DistributionBreakdown:
    r"""Information about the accounts that the payment was distributed to."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    account_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_name'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""Name of the account for the given distribution."""
    bank_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_name'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""The name of the bank that the payment is being deposited to."""
    current_amount: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_amount'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""The amount distributed to this account."""
    current_pay: Optional[Pay] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_pay'), 'exclude': lambda f: f is None }})
    r"""An object representing a monetary amount.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    iso_currency_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null."""
    mask: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mask'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""The last 2-4 alphanumeric characters of an account's official account number."""
    type: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""Type of the account that the paystub was sent to (e.g. 'checking')."""
    unofficial_currency_code: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code'), 'exclude': lambda f: f is DistributionBreakdown.UNSET }})
    r"""The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.

    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """
    

