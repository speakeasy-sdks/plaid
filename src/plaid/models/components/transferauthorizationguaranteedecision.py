"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class TransferAuthorizationGuaranteeDecision(str, Enum):
    r"""Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details."""
    GUARANTEED = 'GUARANTEED'
    NOT_GUARANTEED = 'NOT_GUARANTEED'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'
