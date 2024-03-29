"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assetdetail import AssetDetail
from .assetholder import AssetHolder
from .assetowners import AssetOwners
from .creditfreddiemacassettransactions_voa_2_4 import CreditFreddieMacAssetTransactionsVOA24
from .validationsources import ValidationSources
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacAssetVOA24:
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    UNSET='__SPEAKEASY_UNSET__'
    asset_detail: AssetDetail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_DETAIL') }})
    r"""Details about an asset."""
    asset_holder: AssetHolder = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_HOLDER') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_owners: AssetOwners = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_OWNERS') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    asset_transactions: CreditFreddieMacAssetTransactionsVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ASSET_TRANSACTIONS') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    validation_sources: ValidationSources = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('VALIDATION_SOURCES') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

