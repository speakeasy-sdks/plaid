"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .transferdiligencestatus import TransferDiligenceStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Originator:
    r"""Originator and their status."""
    UNSET='__SPEAKEASY_UNSET__'
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Originator’s client ID."""
    transfer_diligence_status: TransferDiligenceStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_diligence_status') }})
    r"""Originator’s diligence status."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

