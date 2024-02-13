"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .depositswitchcreaterequestoptions import DepositSwitchCreateRequestOptions
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from plaid import utils
from typing import Optional

class DepositSwitchCreateRequestCountryCode(str, Enum):
    r"""ISO-3166-1 alpha-2 country code standard."""
    US = 'US'
    CA = 'CA'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DepositSwitchCreateRequest:
    r"""DepositSwitchCreateRequest defines the request schema for `/deposit_switch/create`"""
    UNSET='__SPEAKEASY_UNSET__'
    target_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_access_token') }})
    r"""Access token for the target Item, typically provided in the Import Item response."""
    target_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_account_id') }})
    r"""Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    country_code: Optional[DepositSwitchCreateRequestCountryCode] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_code'), 'exclude': lambda f: f is DepositSwitchCreateRequest.UNSET }})
    r"""ISO-3166-1 alpha-2 country code standard."""
    options: Optional[DepositSwitchCreateRequestOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    r"""Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

