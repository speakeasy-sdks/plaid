"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningRequestSearchTerms:
    r"""Search inputs for creating a watchlist screening"""
    legal_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_name') }})
    r"""The legal name of the individual being screened."""
    watchlist_program_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watchlist_program_id') }})
    r"""ID of the associated program."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""
    date_of_birth: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    document_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_number'), 'exclude': lambda f: f is None }})
    r"""The numeric or alphanumeric identifier associated with this document."""
    

