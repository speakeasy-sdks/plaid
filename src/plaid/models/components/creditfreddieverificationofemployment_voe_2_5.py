"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditfreddieverificationofemploymentdeal_voe_2_5 import CreditFreddieVerificationOfEmploymentDealVOE25
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditFreddieVerificationOfEmploymentVOE25:
    r"""Verification of Employment Report"""
    deal: CreditFreddieVerificationOfEmploymentDealVOE25 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DEAL') }})
    r"""An object representing a Verification of Employment report."""
    schema_version: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SchemaVersion') }})
    r"""The Verification Of Employment (VOE) schema version."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

