"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .location import Location
from .paymentmeta import PaymentMeta
from .personalfinancecategory import PersonalFinanceCategory
from .transactioncode import TransactionCode
from .transactioncounterparty import TransactionCounterparty
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from enum import Enum
from plaid import utils
from typing import Any, Dict, List, Optional

class TransactionPaymentChannel(str, Enum):
    r"""The channel used to make a payment.
    `online:` transactions that took place online.

    `in store:` transactions that were made at a physical location.

    `other:` transactions that relate to banks, e.g. fees or deposits.

    This field replaces the `transaction_type` field.
    """
    ONLINE = 'online'
    IN_STORE = 'in store'
    OTHER = 'other'

class TransactionType(str, Enum):
    r"""Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.

    `digital:` transactions that took place online.

    `place:` transactions that were made at a physical location.

    `special:` transactions that relate to banks, e.g. fees or deposits.

    `unresolved:` transactions that do not fit into the other three types.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    DIGITAL = 'digital'
    PLACE = 'place'
    SPECIAL = 'special'
    UNRESOLVED = 'unresolved'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Transaction:
    r"""A representation of a transaction"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The ID of the account in which this transaction occurred."""
    account_owner: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_owner') }})
    r"""The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts."""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The settled value of the transaction, denominated in the transactions's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative."""
    authorized_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorized_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date that the transaction was authorized. For posted transactions, the `date` field will indicate the posted date, but `authorized_date` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_date`, when available, is generally preferable to use over the `date` field for posted transactions, as it will generally represent the date the user actually made the transaction. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` )."""
    authorized_datetime: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorized_datetime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date and time when a transaction was authorized in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For posted transactions, the `datetime` field will indicate the posted date, but `authorized_datetime` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_datetime`, when available, is generally preferable to use over the `datetime` field for posted transactions, as it will generally represent the date the user actually made the transaction.

    This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
    """
    category: Optional[List[str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category') }})
    r"""A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).

    All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.

    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    category_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category_id') }})
    r"""The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).

    All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category_id`, as it provides greater accuracy and more meaningful categorization.

    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    date_: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). To receive information about the date that a posted transaction was initiated, see the `authorized_date` field."""
    datetime_: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datetime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date and time when a transaction was posted in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For the date that the transaction was initiated, rather than posted, see the `authorized_datetime` field.

    This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
    """
    iso_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null."""
    location: Location = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    r"""A representation of where a transaction took place"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The merchant name or transaction description.

    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    payment_channel: TransactionPaymentChannel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_channel') }})
    r"""The channel used to make a payment.
    `online:` transactions that took place online.

    `in store:` transactions that were made at a physical location.

    `other:` transactions that relate to banks, e.g. fees or deposits.

    This field replaces the `transaction_type` field.
    """
    payment_meta: PaymentMeta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_meta') }})
    r"""Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.

    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """
    pending: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending') }})
    r"""When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled."""
    pending_transaction_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending_transaction_id') }})
    r"""The ID of a posted transaction's associated pending transaction, where applicable."""
    transaction_code: Optional[TransactionCode] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_code') }})
    r"""An identifier classifying the transaction type.

    This field is only populated for European institutions. For institutions in the US and Canada, this field is set to `null`.

    `adjustment:` Bank adjustment

    `atm:` Cash deposit or withdrawal via an automated teller machine

    `bank charge:` Charge or fee levied by the institution

    `bill payment`: Payment of a bill

    `cash:` Cash deposit or withdrawal

    `cashback:` Cash withdrawal while making a debit card purchase

    `cheque:` Document ordering the payment of money to another person or organization

    `direct debit:` Automatic withdrawal of funds initiated by a third party at a regular interval

    `interest:` Interest earned or incurred

    `purchase:` Purchase made with a debit or credit card

    `standing order:` Payment instructed by the account holder to a third party at a regular interval

    `transfer:` Transfer of money between accounts
    """
    transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})
    r"""The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive."""
    unofficial_currency_code: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unofficial_currency_code') }})
    r"""The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.

    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    check_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('check_number') }})
    r"""The check number of the transaction. This field is only populated for check transactions."""
    counterparties: Optional[List[TransactionCounterparty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('counterparties'), 'exclude': lambda f: f is None }})
    r"""The counterparties present in the transaction. Counterparties, such as the financial institutions, are extracted by Plaid from the raw description."""
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo_url') }})
    r"""The logo associated with the merchant, if available. Formatted as a 100x100 pixels PNG file path."""
    merchant_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_name') }})
    r"""The merchant name, as enriched by Plaid from the `name` field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be `null`."""
    original_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('original_description') }})
    r"""The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/sync` or `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`."""
    personal_finance_category: Optional[PersonalFinanceCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_finance_category') }})
    r"""Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.

    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """
    personal_finance_category_icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_finance_category_icon_url'), 'exclude': lambda f: f is None }})
    r"""A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels."""
    transaction_type: Optional[TransactionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_type'), 'exclude': lambda f: f is None }})
    r"""Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.

    `digital:` transactions that took place online.

    `place:` transactions that were made at a physical location.

    `special:` transactions that relate to banks, e.g. fees or deposits.

    `unresolved:` transactions that do not fit into the other three types.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    website: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('website') }})
    r"""The website associated with the merchant, if available."""
    

