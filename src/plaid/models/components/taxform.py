"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .w2 import W2
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Taxform:
    r"""Data about an official document used to report the user's income to the IRS."""
    document_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_type') }})
    r"""The type of tax document. Currently, the only supported value is `w2`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    doc_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doc_id'), 'exclude': lambda f: f is None }})
    r"""An identifier of the document referenced by the document metadata."""
    w2: Optional[W2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('w2'), 'exclude': lambda f: f is None }})
    r"""W2 is an object that represents income data taken from a W2 tax document."""
    

