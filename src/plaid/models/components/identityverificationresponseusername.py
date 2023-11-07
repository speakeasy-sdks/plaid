"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IdentityVerificationResponseUserName:
    r"""The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise, both fields are guaranteed to be filled."""
    family_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name') }})
    r"""A string with at least one non-whitespace character, with a max length of 100 characters."""
    given_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name') }})
    r"""A string with at least one non-whitespace character, with a max length of 100 characters."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

