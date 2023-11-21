"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .watchlistscreeningdocumenttype import WatchlistScreeningDocumentType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WatchlistScreeningDocument:
    r"""An official document, usually issued by a governing body or institution, with an associated identifier."""
    number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number') }})
    r"""The numeric or alphanumeric identifier associated with this document."""
    type: WatchlistScreeningDocumentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The kind of official document represented by this object.

    `birth_certificate` - A certificate of birth

    `drivers_license` - A license to operate a motor vehicle

    `immigration_number` - Immigration or residence documents

    `military_id` - Identification issued by a military group

    `other` - Any document not covered by other categories

    `passport` - An official passport issue by a government

    `personal_identification` - Any generic personal identification that is not covered by other categories

    `ration_card` - Identification that entitles the holder to rations

    `ssn` - United States Social Security Number

    `student_id` - Identification issued by an educational institution

    `tax_id` - Identification issued for the purpose of collecting taxes

    `travel_document` - Visas, entry permits, refugee documents, etc.

    `voter_id` - Identification issued for the purpose of voting
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
