"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkSessionExitMetadataInstitution:
    r"""An institution object. If the Item was created via Same-Day micro-deposit verification, will be `null`."""
    institution_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id'), 'exclude': lambda f: f is None }})
    r"""The Plaid institution identifier"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The full institution name, such as `Wells Fargo`"""
    

