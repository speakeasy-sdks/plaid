"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayrollItemStatus:
    r"""Details about the status of the payroll item."""
    UNSET='__SPEAKEASY_UNSET__'
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    processing_status: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing_status'), 'exclude': lambda f: f is PayrollItemStatus.UNSET }})
    r"""Denotes the processing status for the verification.

    `UNKNOWN`: The processing status could not be determined.

    `PROCESSING_COMPLETE`: The processing has completed and the user has approved for sharing. The data is available to be retrieved.

    `PROCESSING`: The verification is still processing. The data is not available yet.

    `FAILED`: The processing failed to complete successfully.

    `APPROVAL_STATUS_PENDING`: The processing has completed but the user has not yet approved the sharing of the data.
    """
    

