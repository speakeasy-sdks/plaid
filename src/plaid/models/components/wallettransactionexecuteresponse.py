"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .wallettransactionstatus import WalletTransactionStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransactionExecuteResponse:
    r"""WalletTransactionExecuteResponse defines the response schema for `/wallet/transaction/execute`"""
    UNSET='__SPEAKEASY_UNSET__'
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    status: WalletTransactionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the transaction.

    `AUTHORISING`: The transaction is being processed for validation and compliance.

    `INITIATED`: The transaction has been initiated and is currently being processed.

    `EXECUTED`: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.

    `SETTLED`: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.

    `FAILED`: The transaction failed to process successfully. This is a terminal status.

    `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.
    """
    transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})
    r"""A unique ID identifying the transaction"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

