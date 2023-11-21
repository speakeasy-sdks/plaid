"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .fdxhateoaslink import FDXHateoasLink
from .fdxnotificationcategory import FDXNotificationCategory
from .fdxnotificationpayload import FDXNotificationPayload
from .fdxnotificationpriority import FDXNotificationPriority
from .fdxnotificationseverity import FDXNotificationSeverity
from .fdxnotificationtype import FDXNotificationType
from .fdxparty import FDXParty
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FDXNotification:
    r"""Provides the base fields of a notification. Clients will read the `type` property to determine the expected notification payload"""
    category: FDXNotificationCategory = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category') }})
    r"""Category of Notification"""
    notification_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationId') }})
    r"""Id of notification"""
    notification_payload: FDXNotificationPayload = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPayload') }})
    r"""Custom key-value pairs payload for a notification"""
    publisher: FDXParty = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publisher') }})
    r"""FDX Participant - an entity or person that is a part of a FDX API transaction"""
    sent_on: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentOn'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""ISO 8601 date-time in format 'YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]' according to [IETF RFC3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)"""
    type: FDXNotificationType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of Notification"""
    priority: Optional[FDXNotificationPriority] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority'), 'exclude': lambda f: f is None }})
    r"""Priority of notification"""
    severity: Optional[FDXNotificationSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""Severity level of notification"""
    subscriber: Optional[FDXParty] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriber'), 'exclude': lambda f: f is None }})
    r"""FDX Participant - an entity or person that is a part of a FDX API transaction"""
    url: Optional[FDXHateoasLink] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""REST application constraint (Hypermedia As The Engine Of Application State)"""
    
