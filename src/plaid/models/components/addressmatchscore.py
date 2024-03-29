"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddressMatchScore:
    r"""Score found by matching address provided by the API with the address on the account at the financial institution. The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    is_postal_code_match: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_postal_code_match'), 'exclude': lambda f: f is AddressMatchScore.UNSET }})
    r"""postal code was provided for both and was a match"""
    score: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is AddressMatchScore.UNSET }})
    r"""Match score for address. 100 is a perfect match, 99-90 is a strong match, 89-80 is a partial match, anything below 80 is considered a weak match. Typically, the match threshold should be set to a score of 80 or higher. If the address is missing from either the API or financial institution, this is null."""
    

