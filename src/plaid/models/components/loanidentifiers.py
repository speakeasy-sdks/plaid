"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .loanidentifier import LoanIdentifier
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoanIdentifiers:
    r"""Collection of current and previous identifiers for this loan."""
    loan_identifier: LoanIdentifier = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LOAN_IDENTIFIER') }})
    r"""The information used to identify this loan by various parties to the transaction or other organizations."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

