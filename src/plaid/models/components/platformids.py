"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PlatformIds:
    r"""An object containing a set of ids related to an employee"""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    employee_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_id'), 'exclude': lambda f: f is PlatformIds.UNSET }})
    r"""The ID of an employee as given by their employer"""
    payroll_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payroll_id'), 'exclude': lambda f: f is PlatformIds.UNSET }})
    r"""The ID of an employee as given by their payroll"""
    position_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position_id'), 'exclude': lambda f: f is PlatformIds.UNSET }})
    r"""The ID of the position of the employee"""
    

