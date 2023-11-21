"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class CreditSessionBankEmploymentStatus(str, Enum):
    r"""Status of the Bank Employment Link session.

    `APPROVED`: User has approved and verified their employment.

    `NO_EMPLOYMENTS_FOUND`: We attempted, but were unable to find any employment in the connected account.

    `EMPLOYER_NOT_LISTED`: The user explicitly indicated that they did not see their current or previous employer in the list of employer names found.

    `STARTED`: The user began the bank income portion of the link flow.

    `INTERNAL_ERROR`: The user encountered an internal error.
    """
    APPROVED = 'APPROVED'
    NO_EMPLOYERS_FOUND = 'NO_EMPLOYERS_FOUND'
    EMPLOYER_NOT_LISTED = 'EMPLOYER_NOT_LISTED'