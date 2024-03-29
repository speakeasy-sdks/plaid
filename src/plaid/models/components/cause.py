"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .plaiderrortype import PlaidErrorType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cause:
    r"""An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""
    UNSET='__SPEAKEASY_UNSET__'
    display_message: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_message') }})
    r"""A user-friendly representation of the error code. `null` if the error is not related to user action.

    This may change over time and is not safe for programmatic use.
    """
    error_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_code') }})
    r"""The particular error code. Safe for programmatic use."""
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_message') }})
    r"""A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use."""
    error_type: PlaidErrorType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_type') }})
    r"""A broad categorization of the error. Safe for programmatic use."""
    item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id') }})
    r"""The `item_id` of the Item associated with this webhook, warning, or error"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    causes: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('causes'), 'exclude': lambda f: f is None }})
    r"""In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.

    `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object.
    """
    documentation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentation_url'), 'exclude': lambda f: f is None }})
    r"""The URL of a Plaid documentation page with more information about the error"""
    request_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id'), 'exclude': lambda f: f is None }})
    r"""A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks."""
    status: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is Cause.UNSET }})
    r"""The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook."""
    suggested_action: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suggested_action'), 'exclude': lambda f: f is Cause.UNSET }})
    r"""Suggested steps for resolving the error"""
    

