"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .personalfinancecategory import PersonalFinanceCategory
from .recurringtransactionfrequency import RecurringTransactionFrequency
from .transactionstreamamount import TransactionStreamAmount
from .transactionstreamstatus import TransactionStreamStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionStream:
    r"""A grouping of related transactions"""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The ID of the account to which the stream belongs"""
    average_amount: TransactionStreamAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('average_amount') }})
    r"""Object with data pertaining to an amount on the transaction stream."""
    category: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category') }})
    r"""A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).

    All implementations are encouraged to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.
    """
    category_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category_id') }})
    r"""The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).

    All implementations are encouraged to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.
    """
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""A description of the transaction stream."""
    first_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The posted date of the earliest transaction in the stream."""
    frequency: RecurringTransactionFrequency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    r"""Describes the frequency of the transaction stream.

    `WEEKLY`: Assigned to a transaction stream that occurs approximately every week.

    `BIWEEKLY`: Assigned to a transaction stream that occurs approximately every 2 weeks.

    `SEMI_MONTHLY`: Assigned to a transaction stream that occurs approximately twice per month. This frequency is typically seen for inflow transaction streams.

    `MONTHLY`: Assigned to a transaction stream that occurs approximately every month.

    `ANNUALLY`: Assigned to a transaction stream that occurs approximately every year.

    `UNKNOWN`: Assigned to a transaction stream that does not fit any of the pre-defined frequencies.
    """
    is_active: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active') }})
    r"""Indicates whether the transaction stream is still live."""
    last_amount: TransactionStreamAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_amount') }})
    r"""Object with data pertaining to an amount on the transaction stream."""
    last_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The posted date of the latest transaction in the stream."""
    merchant_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_name') }})
    r"""The merchant associated with the transaction stream."""
    status: TransactionStreamStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The current status of the transaction stream.

    `MATURE`: A `MATURE` recurring stream should have at least 3 transactions and happen on a regular cadence (For Annual recurring stream, we will mark it `MATURE` after 2 instances).

    `EARLY_DETECTION`: When a recurring transaction first appears in the transaction history and before it fulfills the requirement of a mature stream, the status will be `EARLY_DETECTION`.

    `TOMBSTONED`: A stream that was previously in the `EARLY_DETECTION` status will move to the `TOMBSTONED` status when no further transactions were found at the next expected date.

    `UNKNOWN`: A stream is assigned an `UNKNOWN` status when none of the other statuses are applicable.
    """
    stream_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_id') }})
    r"""A unique id for the stream"""
    transaction_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_ids') }})
    r"""An array of Plaid transaction IDs belonging to the stream, sorted by posted date."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    personal_finance_category: Optional[PersonalFinanceCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_finance_category') }})
    r"""Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.

    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """
    

