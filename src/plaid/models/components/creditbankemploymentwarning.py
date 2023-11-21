"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .creditbankemploymentwarningtype import CreditBankEmploymentWarningType
from .creditbankincomecause import CreditBankIncomeCause
from .creditbankincomewarningcode import CreditBankIncomeWarningCode
from dataclasses_json import Undefined, dataclass_json
from plaid import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditBankEmploymentWarning:
    r"""The warning associated with the data that was unavailable for the Bank Employment Report."""
    cause: CreditBankIncomeCause = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cause') }})
    r"""An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""
    warning_code: CreditBankIncomeWarningCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_code') }})
    r"""The warning code identifies a specific kind of warning.
    `IDENTITY_UNAVAILABLE`: Unable to extract identity for the Item
    `TRANSACTIONS_UNAVAILABLE`: Unable to extract transactions for the Item
    `ITEM_UNAPPROVED`: User exited flow before giving permission to share data for the Item
    `REPORT_DELETED`: Report deleted due to customer or consumer request
    `DATA_UNAVAILABLE`: No relevant data was found for the Item
    """
    warning_type: CreditBankEmploymentWarningType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warning_type') }})
    r"""The warning type which will always be `BANK_EMPLOYMENT_WARNING`."""
    
