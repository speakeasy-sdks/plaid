"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .paymentinitiationoptionalrestrictionbacs import PaymentInitiationOptionalRestrictionBacs
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalPaymentInitiationConsentOptions:
    r"""Additional payment consent options"""
    UNSET='__SPEAKEASY_UNSET__'
    bacs: Optional[PaymentInitiationOptionalRestrictionBacs] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs'), 'exclude': lambda f: f is ExternalPaymentInitiationConsentOptions.UNSET }})
    r"""An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account."""
    iban: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban'), 'exclude': lambda f: f is ExternalPaymentInitiationConsentOptions.UNSET }})
    r"""The International Bank Account Number (IBAN) for the payer's account. Where possible, the end user will be able to set up payment consent using only the specified bank account if provided."""
    request_refund_details: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_refund_details'), 'exclude': lambda f: f is ExternalPaymentInitiationConsentOptions.UNSET }})
    r"""When `true`, Plaid will attempt to request refund details from the payee's financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the `/payment_initiation/payment/get` response."""
    

