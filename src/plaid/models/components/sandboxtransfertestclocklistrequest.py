"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SandboxTransferTestClockListRequest:
    r"""Defines the request schema for `/sandbox/transfer/test_clock/list`"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    count: Optional[int] = dataclasses.field(default=25, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""The maximum number of test clocks to return."""
    end_virtual_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_virtual_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The end virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    r"""The number of test clocks to skip before returning results."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    start_virtual_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_virtual_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    r"""The start virtual timestamp of test clocks to return. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    

