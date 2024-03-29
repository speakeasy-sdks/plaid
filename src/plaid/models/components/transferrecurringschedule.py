"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transferscheduleintervalunit import TransferScheduleIntervalUnit
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferRecurringSchedule:
    r"""The schedule that the recurring transfer will be executed on."""
    UNSET='__SPEAKEASY_UNSET__'
    interval_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval_count') }})
    r"""The number of recurring `interval_units` between originations. The recurring interval(before holiday adjustment) is calculated by multiplying `interval_unit` and `interval_count`.
    For instance, to schedule a recurring transfer which originates once every two weeks, set `interval_unit` = `week` and `interval_count` = 2.
    """
    interval_execution_day: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval_execution_day') }})
    r"""The day of the interval on which to schedule the transfer.

    If the `interval_unit` is `week`, `interval_execution_day` should be an integer from 1 (Monday) to 5 (Friday).

    If the `interval_unit` is `month`, `interval_execution_day` should be an integer indicating which day of the month to make the transfer on. Integers from 1 to 28 can be used to make a transfer on that day of the month. Negative integers from -1 to -5 can be used to make a transfer relative to the end of the month. To make a transfer on the last day of the month, use -1; to make the transfer on the second-to-last day, use -2, and so on.

    The transfer will be originated on next available banking day if the designated day is a non banking day.
    """
    interval_unit: TransferScheduleIntervalUnit = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval_unit') }})
    r"""The unit of the recurring interval."""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will begin on the first `interval_execution_day` on or after the `start_date`.

    If the first `interval_execution_day` on or after the start date is also the same day that `/transfer/recurring/create` was called, the bank *may* make the first payment on that day, but it is not guaranteed to do so.
    """
    end_date: Optional[date] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is TransferRecurringSchedule.UNSET }})
    r"""A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will end on the last `interval_execution_day` on or before the `end_date`.
    If the `interval_execution_day` between the start date and the end date (inclusive) is also the same day that `/transfer/recurring/create` was called, the bank *may* make a payment on that day, but it is not guaranteed to do so.
    """
    

