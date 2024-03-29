"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentinitiationconsentstatus import PaymentInitiationConsentStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationConsentCreateResponse:
    r"""PaymentInitiationConsentCreateResponse defines the response schema for `/payment_initiation/consent/create`"""
    UNSET='__SPEAKEASY_UNSET__'
    consent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_id') }})
    r"""A unique ID identifying the payment consent."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    status: PaymentInitiationConsentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the payment consent.

    `UNAUTHORISED`: Consent created, but requires user authorisation.

    `REJECTED`: Consent authorisation was rejected by the user and/or the bank.

    `AUTHORISED`: Consent is active and ready to be used.

    `REVOKED`: Consent has been revoked and can no longer be used.

    `EXPIRED`: Consent is no longer valid.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

