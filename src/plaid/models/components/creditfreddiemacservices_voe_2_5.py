"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddiemacservice_voe_2_5 import CreditFreddieMacServiceVOE25
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieMacServicesVOE25:
    r"""A collection of objects that describe requests and responses for services."""
    service: CreditFreddieMacServiceVOE25 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SERVICE') }})
    r"""A collection of details related to a fulfillment service or product in terms of request, process and result."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

