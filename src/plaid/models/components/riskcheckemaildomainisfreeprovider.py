"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class RiskCheckEmailDomainIsFreeProvider(str, Enum):
    r"""Indicates whether the email address domain is a free provider such as Gmail or Hotmail if known."""
    YES = 'yes'
    NO = 'no'
    NO_DATA = 'no_data'
