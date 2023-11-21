"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .beaconaudittrail import BeaconAuditTrail
from .beaconuserdata import BeaconUserData
from .beaconuserstatus import BeaconUserStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BeaconUserCreateResponse:
    r"""A Beacon User represents an end user that has been scanned against the Beacon Network."""
    audit_trail: BeaconAuditTrail = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audit_trail') }})
    r"""Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""
    client_user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id') }})
    r"""A unique ID that identifies the end user in your system. This ID can also be used to associate user-specific data from other Plaid products. Financial Account Matching requires this field and the `/link/token/create` `client_user_id` to be consistent. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated Beacon User."""
    program_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('program_id') }})
    r"""ID of the associated Beacon Program."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    status: BeaconUserStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""A status of a Beacon User.

    `rejected`: The Beacon User has been rejected for fraud. Users can be automatically or manually rejected.

    `pending_review`: The Beacon User has been marked for review.

    `cleared`: The Beacon User has been cleared of fraud.
    """
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp. This field indicates the last time the resource was modified."""
    user: BeaconUserData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""A Beacon User's data and resulting analysis when checked against duplicate records and the Beacon Fraud Network."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
