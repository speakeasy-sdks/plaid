"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .linksessionexit import LinkSessionExit
from .linksessionsuccess import LinkSessionSuccess
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenGetSessionsResponse:
    r"""An object containing information about a link session."""
    UNSET='__SPEAKEASY_UNSET__'
    link_session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_session_id') }})
    r"""The unique ID for the link session."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    finished_at: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finished_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is LinkTokenGetSessionsResponse.UNSET }})
    r"""The timestamp at which the link session was finished, if available, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    on_exit: Optional[LinkSessionExit] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('on_exit'), 'exclude': lambda f: f is LinkTokenGetSessionsResponse.UNSET }})
    r"""An object representing an [onExit](https://plaid.com/docs/link/web/#onexit) callback from Link."""
    on_success: Optional[LinkSessionSuccess] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('on_success'), 'exclude': lambda f: f is LinkTokenGetSessionsResponse.UNSET }})
    r"""An object representing an [onSuccess](https://plaid.com/docs/link/web/#onsuccess) callback from Link."""
    started_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('started_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The timestamp at which the link session was first started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    

