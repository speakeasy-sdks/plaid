"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .accountassets import AccountAssets
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportItem:
    r"""A representation of an Item within an Asset Report."""
    UNSET='__SPEAKEASY_UNSET__'
    accounts: List[AccountAssets] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    r"""Data about each of the accounts open on the Item."""
    date_last_updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_last_updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    institution_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id') }})
    r"""The id of the financial institution associated with the Item."""
    institution_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_name') }})
    r"""The full financial institution name associated with the Item."""
    item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id') }})
    r"""The `item_id` of the Item associated with this webhook, warning, or error"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

