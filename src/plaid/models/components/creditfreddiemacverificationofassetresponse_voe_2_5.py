"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacassets_voe_2_5 import CreditFreddieMacAssetsVOE25
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacVerificationOfAssetResponseVOE25:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    assets: CreditFreddieMacAssetsVOE25 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSETS') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

