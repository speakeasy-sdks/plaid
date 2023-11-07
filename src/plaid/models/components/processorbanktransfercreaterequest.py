"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .achclass import ACHClass
from .banktransfernetwork import BankTransferNetwork
from .banktransfertype import BankTransferType
from .banktransferuser import BankTransferUserInput
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessorBankTransferCreateRequest:
    r"""Defines the request schema for `/processor/bank_transfer/create`"""
    amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the bank transfer (decimal string with two digits of precision e.g. \\"10.00\\")."""
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""The transfer description. Maximum of 10 characters."""
    idempotency_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key') }})
    r"""A random key provided by the client, per unique bank transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created.
    """
    iso_currency_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iso_currency_code') }})
    r"""The currency of the transfer amount – should be set to \\"USD\\"."""
    network: BankTransferNetwork = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network') }})
    r"""The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`."""
    processor_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processor_token') }})
    r"""The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>`"""
    type: BankTransferType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    user: BankTransferUserInput = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The legal name and other information for the account holder."""
    ach_class: Optional[ACHClass] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach_class'), 'exclude': lambda f: f is None }})
    r"""Specifies the use case of the transfer. Required for transfers on an ACH network.

    `\"ccd\"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `\"ppd\"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `\"tel\"` - Telephone-Initiated Entry

    `\"web\"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    custom_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_tag') }})
    r"""An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters."""
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    The JSON values must be Strings (no nested JSON objects allowed)
    Only ASCII characters may be used
    Maximum of 50 key/value pairs
    Maximum key length of 40 characters
    Maximum value length of 500 characters
    """
    origination_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_account_id') }})
    r"""Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified."""
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    

