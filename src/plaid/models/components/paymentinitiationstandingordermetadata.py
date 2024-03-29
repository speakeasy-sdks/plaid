"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentscheduleinterval import PaymentScheduleInterval
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationStandingOrderMetadata:
    r"""Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""
    UNSET='__SPEAKEASY_UNSET__'
    supports_standing_order_end_date: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supports_standing_order_end_date') }})
    r"""Indicates whether the institution supports closed-ended standing orders by providing an end date."""
    supports_standing_order_negative_execution_days: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supports_standing_order_negative_execution_days') }})
    r"""This is only applicable to `MONTHLY` standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a `MONTHLY` standing order relative to the end of the month."""
    valid_standing_order_intervals: List[PaymentScheduleInterval] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('valid_standing_order_intervals') }})
    r"""A list of the valid standing order intervals supported by the institution."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

