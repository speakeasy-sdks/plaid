"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportUser:
    r"""The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    client_user_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_user_id'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""An identifier you determine and submit for the user."""
    email: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's email address."""
    first_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's first name. Required for the Fannie Mae Day 1 Certainty™ program."""
    last_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's last name.  Required for the Fannie Mae Day 1 Certainty™ program."""
    middle_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('middle_name'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's middle name"""
    phone_number: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's phone number, in E.164 format: +{countrycode}{number}. For example: \\"+14151234567\\". Phone numbers provided in other formats will be parsed on a best-effort basis."""
    ssn: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssn'), 'exclude': lambda f: f is AssetReportUser.UNSET }})
    r"""The user's Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.

    Format: \"ddd-dd-dddd\" 
    """
    

