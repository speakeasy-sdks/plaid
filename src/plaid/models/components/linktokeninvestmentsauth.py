"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenInvestmentsAuth:
    r"""Configuration parameters for the Investments Auth Product"""
    UNSET='__SPEAKEASY_UNSET__'
    manual_entry_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manual_entry_enabled'), 'exclude': lambda f: f is LinkTokenInvestmentsAuth.UNSET }})
    r"""If `true`, show institutions that use the manual entry fallback flow."""
    masked_number_match_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('masked_number_match_enabled'), 'exclude': lambda f: f is LinkTokenInvestmentsAuth.UNSET }})
    r"""If `true`, show institutions that use the masked number match fallback flow."""
    

