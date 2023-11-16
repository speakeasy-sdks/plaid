"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .externalpaymentrefunddetails import ExternalPaymentRefundDetails
from .externalpaymentscheduleget import ExternalPaymentScheduleGet
from .paymentamount import PaymentAmount
from .paymentamountrefunded import PaymentAmountRefunded
from .paymentinitiationpaymentstatus import PaymentInitiationPaymentStatus
from .paymentscheme import PaymentScheme
from .senderbacsnullable import SenderBACSNullable
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInitiationPayment:
    r"""PaymentInitiationPayment defines a payment initiation payment"""
    amount: PaymentAmount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount and currency of a payment"""
    bacs: Optional[SenderBACSNullable] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs') }})
    r"""An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""
    iban: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban') }})
    r"""The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call."""
    last_status_update: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_status_update'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time of the last time the `status` was updated, in IS0 8601 format"""
    payment_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_id') }})
    r"""The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive."""
    recipient_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_id') }})
    r"""The ID of the recipient"""
    reference: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference') }})
    r"""A reference for the payment."""
    status: PaymentInitiationPaymentStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the payment.

    `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.

    `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.

    `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.

    `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.

    `PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.

    `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.

    `PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.

    `PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.

    `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).

    `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.

    `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.

    Deprecated:
    These statuses will be removed in a future release.

    `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.

    `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.

    `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    adjusted_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjusted_reference') }})
    r"""The value of the reference sent to the bank after adjustment to pass bank validation rules."""
    adjusted_scheme: Optional[PaymentScheme] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjusted_scheme') }})
    r"""Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.

    `LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.

    `LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.

    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.
    """
    amount_refunded: Optional[PaymentAmountRefunded] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_refunded') }})
    r"""The amount and currency of a payment"""
    consent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consent_id') }})
    r"""The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent."""
    refund_details: Optional[ExternalPaymentRefundDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_details') }})
    r"""Details about external payment refund"""
    refund_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refund_ids') }})
    r"""Refund IDs associated with the payment."""
    schedule: Optional[ExternalPaymentScheduleGet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule') }})
    r"""The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up as a standing order. If no schedule is specified, the payment will be executed only once."""
    scheme: Optional[PaymentScheme] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme') }})
    r"""Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.

    `LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.

    `LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.

    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.
    """
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})
    r"""The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts."""
    wallet_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_id') }})
    r"""The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""
    

