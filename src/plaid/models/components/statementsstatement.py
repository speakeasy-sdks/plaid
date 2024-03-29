"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StatementsStatement:
    r"""A statement's metadata associated with an account"""
    UNSET='__SPEAKEASY_UNSET__'
    month: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('month') }})
    r"""Month of the year. Possible values: 1 through 12 (January through December)."""
    statement_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statement_id') }})
    r"""Plaid's unique identifier for the statement."""
    year: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year') }})
    r"""Year. Possible values: 2010-{current_year}."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

