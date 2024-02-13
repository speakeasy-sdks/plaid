"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .partnerendcustomeroauthinstitutionapplicationstatus import PartnerEndCustomerOAuthInstitutionApplicationStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PartnerEndCustomerOAuthInstitutionEnvironments:
    r"""Registration statuses by environment."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    development: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('development'), 'exclude': lambda f: f is None }})
    r"""The registration status for the end customer's application."""
    production: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('production'), 'exclude': lambda f: f is None }})
    r"""The registration status for the end customer's application."""
    

