"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferAuthorizationDevice:
    r"""Information about the device being used to initiate the authorization."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    ip_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_address'), 'exclude': lambda f: f is None }})
    r"""The IP address of the device being used to initiate the authorization. Required when the end-user is present at authorization create time."""
    user_agent: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_agent'), 'exclude': lambda f: f is None }})
    r"""The user agent of the device being used to initiate the authorization. Required when the end-user is present at authorization create time."""
    
