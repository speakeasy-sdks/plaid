"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Category:
    r"""Information describing a transaction category"""
    category_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category_id') }})
    r"""An identifying number for the category. `category_id` is a Plaid-specific identifier and does not necessarily correspond to merchant category codes."""
    group: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group') }})
    r"""`place` for physical transactions or `special` for other transactions such as bank charges."""
    hierarchy: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hierarchy') }})
    r"""A hierarchical array of the categories to which this `category_id` belongs."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

