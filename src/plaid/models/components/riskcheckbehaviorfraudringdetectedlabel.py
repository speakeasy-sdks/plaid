"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class RiskCheckBehaviorFraudRingDetectedLabel(str, Enum):
    r"""Field describing the outcome of a fraud ring behavior risk check.

    `yes` indicates that fraud ring activity was detected.

    `no` indicates that fraud ring activity was not detected.

    `no_data` indicates there was not enough information available to give an accurate signal.
    """
    YES = 'yes'
    NO = 'no'
    NO_DATA = 'no_data'
