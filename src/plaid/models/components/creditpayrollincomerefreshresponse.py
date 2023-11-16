"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditPayrollIncomeRefreshResponse:
    r"""CreditPayrollIncomeRefreshResponse defines the response schema for `/credit/payroll_income/refresh`"""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    verification_refresh_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verification_refresh_status') }})
    r"""The verification refresh status. One of the following:

    `\"USER_PRESENCE_REQUIRED\"` User presence is required to refresh an income verification.
    `\"SUCCESSFUL\"` The income verification refresh was successful.
    `\"NOT_FOUND\"` No new data was found after the income verification refresh.
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

