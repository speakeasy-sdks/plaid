"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .beaconaudittrail import BeaconAuditTrail
from .beaconreporttype import BeaconReportType
from .fraudamount import FraudAmount
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconReportCreateResponse:
    r"""A Beacon Report describes the type of fraud committed by a user as well as the date the fraud was committed and the total amount of money lost due to the fraud incident.

    This information is used to block similar fraud attempts on your platform as well as alert other companies who screen a user with matching identity information.
    Other companies will not receive any new identity information, just what matched, plus information such as industry, type of fraud, and date of fraud.

    You can manage your fraud reports by adding, deleting, or editing reports as you get additional information on fraudulent users.
    """
    audit_trail: BeaconAuditTrail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_trail') }})
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    beacon_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('beacon_user_id') }})
    r"""ID of the associated Beacon User."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    fraud_amount: FraudAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fraud_amount') }})
    r"""The amount and currency of the fraud or attempted fraud.
    `fraud_amount` should be omitted to indicate an unknown fraud amount.
    """
    fraud_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fraud_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated Beacon Report."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    type: BeaconReportType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of Beacon Report.

    `first_party`: If this is the same individual as the one who submitted the KYC.

    `third_party`: If this is a different individual from the one who submitted the KYC.

    `synthetic`: If this is an individual using fabricated information.

    `account_takeover`: If this individual's account was compromised.

    `unknown`: If you aren't sure who committed the fraud.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

