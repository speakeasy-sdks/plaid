"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paystubaddress import PaystubAddress
from .taxpayerid import TaxpayerID
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Employee:
    r"""Data about the employee."""
    address: PaystubAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""Address on the paystub"""
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the employee."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    marital_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('marital_status') }})
    r"""Marital status of the employee - either `single` or `married`."""
    taxpayer_id: Optional[TaxpayerID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxpayer_id'), 'exclude': lambda f: f is None }})
    r"""Taxpayer ID of the individual receiving the paystub."""
    

