"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .sweepstatus import SweepStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferSweep:
    r"""Describes a sweep of funds to / from the sweep account.

    A sweep is associated with many sweep events (events of type `swept` or `return_swept`) which can be retrieved by invoking the `/transfer/event/list` endpoint with the corresponding `sweep_id`.

    `swept` events occur when the transfer amount is credited or debited from your sweep account, depending on the `type` of the transfer. `return_swept` events occur when a transfer is returned and Plaid undoes the credit or debit.

    The total sum of the `swept` and `return_swept` events is equal to the `amount` of the sweep Plaid creates and matches the amount of the entry on your sweep account ledger.
    """
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. \\"-10.00\\")

    If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep account and Plaid are balanced.
    """
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The datetime when the sweep occurred, in RFC 3339 format."""
    funding_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id') }})
    r"""The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Identifier of the sweep."""
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the sweep, e.g. \\"USD\\"."""
    settled: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settled'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date when the sweep settled, in the YYYY-MM-DD format."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    status: Optional[SweepStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of a sweep transfer

    `\"pending\"` - The sweep is currently pending
    `\"posted\"` - The sweep has been posted
    `\"settled\"` - The sweep has settled
    `\"returned\"` - The sweep has been returned
    `\"failed\"` - The sweep has failed
    """
    

