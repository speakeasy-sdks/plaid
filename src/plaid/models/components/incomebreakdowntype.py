"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class IncomeBreakdownType(str, Enum):
    r"""The type of income. Possible values include:
      `\"regular\"`: regular income
      `\"overtime\"`: overtime income
      `\"bonus\"`: bonus income
    """
    BONUS = 'bonus'
    OVERTIME = 'overtime'
    REGULAR = 'regular'
