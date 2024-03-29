"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .statuses import Statuses
from .verificationofasset import VerificationOfAsset
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Service:
    r"""A collection of details related to a fulfillment service or product in terms of request, process and result."""
    UNSET='__SPEAKEASY_UNSET__'
    statuses: Statuses = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('STATUSES') }})
    r"""A collection of STATUS containers."""
    verification_of_asset: VerificationOfAsset = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VERIFICATION_OF_ASSET') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

