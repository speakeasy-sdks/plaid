"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LastDataAccessTimes:
    r"""Describes the last time each datatype was accessed by an application."""
    UNSET='__SPEAKEASY_UNSET__'
    account_balance_info: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_balance_info'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time account_balance_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    account_routing_number: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_routing_number'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time account_routing_number was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    application_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application_id') }})
    r"""ID of the application accessing data."""
    contact_details: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact_details'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time contact_details was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    credit_and_loans: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_and_loans'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time credit_and_loans was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    investments: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('investments'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time investments was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    payroll_info: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payroll_info'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time payroll_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    transaction_risk_info: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_risk_info'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time transaction_risk_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    transactions: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The last time transactions was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

