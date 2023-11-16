"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenCreateRequestDepositSwitch:
    r"""Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array."""
    deposit_switch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deposit_switch_id') }})
    r"""The `deposit_switch_id` provided by the `/deposit_switch/create` endpoint."""
    

