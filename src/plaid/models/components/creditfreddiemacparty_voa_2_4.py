"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacpartyindividual_voa_2_4 import CreditFreddieMacPartyIndividualVOA24
from .roles import Roles
from .taxpayeridentifiers import TaxpayerIdentifiers
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacPartyVOA24:
    r"""A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider."""
    UNSET='__SPEAKEASY_UNSET__'
    individual: CreditFreddieMacPartyIndividualVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('INDIVIDUAL') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    roles: Roles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ROLES') }})
    r"""Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""
    taxpayer_identifiers: TaxpayerIdentifiers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('TAXPAYER_IDENTIFIERS') }})
    r"""The collection of TAXPAYER_IDENTIFICATION elements"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

