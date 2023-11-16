"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PSLFStatus:
    r"""Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`)."""
    estimated_eligibility_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('estimated_eligibility_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    payments_made: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments_made') }})
    r"""The number of qualifying payments that have been made."""
    payments_remaining: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments_remaining') }})
    r"""The number of qualifying payments remaining."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

