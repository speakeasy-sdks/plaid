"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .recurringtransfernullable import RecurringTransferNullable
from .transferauthorizationdecision import TransferAuthorizationDecision
from .transferauthorizationdecisionrationale import TransferAuthorizationDecisionRationale
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransferRecurringCreateResponse:
    r"""Defines the response schema for `/transfer/recurring/create`"""
    decision: TransferAuthorizationDecision = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decision') }})
    r"""A decision regarding the proposed transfer.

    `approved` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `ITEM_LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.

    `declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details.
    """
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    decision_rationale: Optional[TransferAuthorizationDecisionRationale] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decision_rationale') }})
    r"""The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions."""
    recurring_transfer: Optional[RecurringTransferNullable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recurring_transfer') }})
    r"""Represents a recurring transfer within the Transfers API."""
    
