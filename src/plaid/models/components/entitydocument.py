"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entitydocumenttype import EntityDocumentType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDocument:
    r"""An official document, usually issued by a governing body or institution, with an associated identifier."""
    UNSET='__SPEAKEASY_UNSET__'
    number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number') }})
    r"""The numeric or alphanumeric identifier associated with this document."""
    type: EntityDocumentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The kind of official document represented by this object.

    `bik` - Russian bank code

    `business_number` - A number that uniquely identifies the business within a category of businesses

    `imo` - Number assigned to the entity by the International Maritime Organization

    `other` - Any document not covered by other categories

    `swift` - Number identifying a bank and branch.

    `tax_id` - Identification issued for the purpose of collecting taxes
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

