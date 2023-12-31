"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class CreditAccountSubtype(str, Enum):
    r"""Valid account subtypes for credit accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-credit)."""
    CREDIT_CARD = 'credit card'
    PAYPAL = 'paypal'
    ALL = 'all'
