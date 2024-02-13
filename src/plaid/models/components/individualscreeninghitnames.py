"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .weakaliasdetermination import WeakAliasDetermination
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IndividualScreeningHitNames:
    r"""Name information for the associated individual watchlist hit"""
    UNSET='__SPEAKEASY_UNSET__'
    full: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full') }})
    r"""The full name of the individual, including all parts."""
    is_primary: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_primary') }})
    r"""Primary names are those most commonly used to refer to this person. Only one name will ever be marked as primary."""
    weak_alias_determination: WeakAliasDetermination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weak_alias_determination') }})
    r"""Names that are explicitly marked as low quality either by their `source` list, or by `plaid` by a series of additional checks done by Plaid. Plaid does not ever surface a hit as a result of a weak name alone. If a name has no quality issues, this value will be `none`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

