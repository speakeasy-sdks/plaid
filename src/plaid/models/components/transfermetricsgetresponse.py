"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferMetricsGetResponse:
    r"""Defines the response schema for `/transfer/metrics/get`"""
    daily_credit_transfer_volume: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('daily_credit_transfer_volume') }})
    r"""Sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. \\"10.00\\")."""
    daily_debit_transfer_volume: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('daily_debit_transfer_volume') }})
    r"""Sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. \\"10.00\\")."""
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the dollar amount, e.g. \\"USD\\"."""
    monthly_credit_transfer_volume: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthly_credit_transfer_volume') }})
    r"""Sum of dollar amount of credit transfers in current calendar month (decimal string with two digits of precision e.g. \\"10.00\\")."""
    monthly_debit_transfer_volume: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthly_debit_transfer_volume') }})
    r"""Sum of dollar amount of debit transfers in current calendar month (decimal string with two digits of precision e.g. \\"10.00\\")."""
    monthly_transfer_volume: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthly_transfer_volume') }})
    r"""Sum of dollar amount of credit and debit transfers in current calendar month (decimal string with two digits of precision e.g. \\"10.00\\")."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
