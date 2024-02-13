"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transfertestclock import TransferTestClock
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SandboxTransferTestClockListResponse:
    r"""Defines the response schema for `/sandbox/transfer/test_clock/list`"""
    UNSET='__SPEAKEASY_UNSET__'
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    test_clocks: List[TransferTestClock] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test_clocks') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

