"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacloans_voa_2_4 import CreditFreddieMacLoansVOA24
from .creditfreddiemacparties_voa_2_4 import CreditFreddieMacPartiesVOA24
from .creditfreddiemacservices_voe_2_5 import CreditFreddieMacServicesVOE25
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieVerificationOfEmploymentDealVOE25:
    r"""An object representing a Verification of Employment report."""
    UNSET='__SPEAKEASY_UNSET__'
    loans: CreditFreddieMacLoansVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LOANS') }})
    r"""A collection of loans that are part of a single deal."""
    parties: CreditFreddieMacPartiesVOA24 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PARTIES') }})
    r"""A collection of objects that define specific parties to a deal. This includes the direct participating parties, such as borrower and seller and the indirect parties such as the credit report provider."""
    services: CreditFreddieMacServicesVOE25 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SERVICES') }})
    r"""A collection of objects that describe requests and responses for services."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

