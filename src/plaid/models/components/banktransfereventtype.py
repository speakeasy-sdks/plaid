"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BankTransferEventType(str, Enum):
    r"""The type of event that this bank transfer represents.

    `pending`: A new transfer was created; it is in the pending state.

    `cancelled`: The transfer was cancelled by the client.

    `failed`: The transfer failed, no funds were moved.

    `posted`: The transfer has been successfully submitted to the payment network.

    `reversed`: A posted transfer was reversed.
    """
    PENDING = 'pending'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    POSTED = 'posted'
    REVERSED = 'reversed'