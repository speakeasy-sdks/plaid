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
class TransferListRequest:
    r"""Defines the request schema for `/transfer/list`"""
    UNSET='__SPEAKEASY_UNSET__'
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    count: Optional[int] = dataclasses.field(default=25, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""The maximum number of transfers to return."""
    end_date: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is TransferListRequest.UNSET }})
    r"""The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    funding_account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('funding_account_id'), 'exclude': lambda f: f is TransferListRequest.UNSET }})
    r"""Filter transfers to only those with the specified `funding_account_id`."""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    r"""The number of transfers to skip before returning results."""
    origination_account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id'), 'exclude': lambda f: f is TransferListRequest.UNSET }})
    r"""Filter transfers to only those originated through the specified origination account.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    originator_client_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originator_client_id'), 'exclude': lambda f: f is TransferListRequest.UNSET }})
    r"""Filter transfers to only those with the specified originator client."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    start_date: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is TransferListRequest.UNSET }})
    r"""The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""
    

