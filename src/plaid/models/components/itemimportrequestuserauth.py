"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ItemImportRequestUserAuth:
    r"""Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts"""
    auth_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_token') }})
    r"""Authorization token Plaid will use to aggregate this user’s accounts"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""Opaque user identifier"""
    

