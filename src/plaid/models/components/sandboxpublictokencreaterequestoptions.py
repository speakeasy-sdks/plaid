"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .sandboxpublictokencreaterequestoptionsincomeverification import SandboxPublicTokenCreateRequestOptionsIncomeVerification
from .sandboxpublictokencreaterequestoptionstransactions import SandboxPublicTokenCreateRequestOptionsTransactions
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SandboxPublicTokenCreateRequestOptions:
    r"""An optional set of options to be used when configuring the Item. If specified, must not be `null`."""
    income_verification: Optional[SandboxPublicTokenCreateRequestOptionsIncomeVerification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_verification'), 'exclude': lambda f: f is None }})
    r"""A set of parameters for income verification options. This field is required if `income_verification` is included in the `initial_products` array."""
    override_password: Optional[str] = dataclasses.field(default='pass_good', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('override_password') }})
    r"""Test password to use for the creation of the Sandbox Item. Default value is `pass_good`."""
    override_username: Optional[str] = dataclasses.field(default='user_good', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('override_username') }})
    r"""Test username to use for the creation of the Sandbox Item. Default value is `user_good`."""
    transactions: Optional[SandboxPublicTokenCreateRequestOptionsTransactions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'exclude': lambda f: f is None }})
    r"""An optional set of parameters corresponding to transactions options."""
    webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook'), 'exclude': lambda f: f is None }})
    r"""Specify a webhook to associate with the new Item."""
    
