"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class PaystubPayFrequency(str, Enum):
    r"""The frequency at which the employee is paid. Possible values: `MONTHLY`, `BI-WEEKLY`, `WEEKLY`, `SEMI-MONTHLY`."""
    MONTHLY = 'MONTHLY'
    BI_WEEKLY = 'BI-WEEKLY'
    WEEKLY = 'WEEKLY'
    SEMI_MONTHLY = 'SEMI-MONTHLY'
