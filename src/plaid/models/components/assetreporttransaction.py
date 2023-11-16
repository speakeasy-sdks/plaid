"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assetreporttransactiontype import AssetReportTransactionType
from .creditcategory import CreditCategory
from .location import Location
from .paymentmeta import PaymentMeta
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportTransaction:
    r"""A transaction on the asset report"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The ID of the account in which this transaction occurred."""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The settled value of the transaction, denominated in the transaction's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative."""
    date_: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` )."""
    iso_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null."""
    original_description: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('original_description') }})
    r"""The string returned by the financial institution to describe the transaction."""
    pending: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending') }})
    r"""When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled."""
    transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})
    r"""The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive."""
    unofficial_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code') }})
    r"""The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.

    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `unofficial_currency_code`s.
    """
    account_owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_owner') }})
    r"""The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    category: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category') }})
    r"""A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).

    This field will only appear in an Asset Report with Insights.
    """
    category_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category_id') }})
    r"""The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).

    This field will only appear in an Asset Report with Insights.
    """
    check_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('check_number') }})
    r"""The check number of the transaction. This field is only populated for check transactions."""
    credit_category: Optional[CreditCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_category') }})
    r"""Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such use cases.

    See the [`taxonomy csv file`](https://plaid.com/documents/credit-category-taxonomy.csv) for a full list of credit categories.
    """
    date_transacted: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_transacted') }})
    r"""The date on which the transaction took place, in IS0 8601 format."""
    income_source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_source_id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier for an income source."""
    location: Optional[Location] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    r"""A representation of where a transaction took place"""
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_name') }})
    r"""The merchant name, as enriched by Plaid from the `name` field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be `null`."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The merchant name or transaction description.

    This field will only appear in an Asset Report with Insights.
    """
    payment_meta: Optional[PaymentMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_meta'), 'exclude': lambda f: f is None }})
    r"""Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.

    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    pending_transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending_transaction_id') }})
    r"""The ID of a posted transaction's associated pending transaction, where applicable."""
    transaction_type: Optional[AssetReportTransactionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_type'), 'exclude': lambda f: f is None }})
    r"""`digital:` transactions that took place online.

    `place:` transactions that were made at a physical location.

    `special:` transactions that relate to banks, e.g. fees or deposits.

    `unresolved:` transactions that do not fit into the other three types.
    """
    

