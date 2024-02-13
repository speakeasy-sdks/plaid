"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .authsupportedmethods import AuthSupportedMethods
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthMetadata:
    r"""Metadata that captures information about the Auth features of an institution."""
    UNSET='__SPEAKEASY_UNSET__'
    supported_methods: Optional[AuthSupportedMethods] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supported_methods') }})
    r"""Metadata specifically related to which auth methods an institution supports."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

