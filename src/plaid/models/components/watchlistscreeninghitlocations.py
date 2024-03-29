"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningHitLocations:
    r"""Location information for the associated individual watchlist hit"""
    UNSET='__SPEAKEASY_UNSET__'
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""
    full: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full') }})
    r"""The full location string, potentially including elements like street, city, postal codes and country codes. Note that this is not necessarily a complete or well-formatted address."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

