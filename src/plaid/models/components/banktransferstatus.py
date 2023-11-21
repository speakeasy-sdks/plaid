"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BankTransferStatus(str, Enum):
    r"""The status of the transfer."""
    PENDING = 'pending'
    POSTED = 'posted'
    CANCELLED = 'cancelled'
    FAILED = 'failed'
    REVERSED = 'reversed'