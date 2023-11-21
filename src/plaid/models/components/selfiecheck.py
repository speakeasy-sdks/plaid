"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .selfiecheckselfie import SelfieCheckSelfie
from .selfiecheckstatus import SelfieCheckStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SelfieCheck:
    r"""Additional information for the `selfie_check` step. This field will be `null` unless `steps.selfie_check` has reached a terminal state of either `success` or `failed`."""
    selfies: List[SelfieCheckSelfie] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selfies') }})
    r"""An array of selfies submitted to the `selfie_check` step. Each entry represents one user submission."""
    status: SelfieCheckStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The outcome status for the associated Identity Verification attempt's `selfie_check` step. This field will always have the same value as `steps.selfie_check`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
