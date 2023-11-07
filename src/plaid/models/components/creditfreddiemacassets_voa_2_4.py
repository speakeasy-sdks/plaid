"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacasset_voa_2_4 import CreditFreddieMacAssetVOA24
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacAssetsVOA24:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset: List[CreditFreddieMacAssetVOA24] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

