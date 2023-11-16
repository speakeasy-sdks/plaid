"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditbankincomeerrortype import CreditBankIncomeErrorType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CraBankIncomeCause:
    r"""An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""
    display_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_message') }})
    r"""A user-friendly representation of the error code. null if the error is not related to user action.
    This may change over time and is not safe for programmatic use.
    """
    error_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_code') }})
    r"""We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. Error fields will be `null` if no error has occurred."""
    error_message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_message') }})
    r"""A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use."""
    error_type: CreditBankIncomeErrorType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error_type') }})
    r"""A broad categorization of the error. Safe for programmatic use."""
    

