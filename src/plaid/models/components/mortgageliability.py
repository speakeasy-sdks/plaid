"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .mortgageinterestrate import MortgageInterestRate
from .mortgagepropertyaddress import MortgagePropertyAddress
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MortgageLiability:
    r"""Contains details about a mortgage account."""
    UNSET='__SPEAKEASY_UNSET__'
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""The ID of the account that this liability belongs to."""
    account_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""The account number of the loan."""
    current_late_fee: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_late_fee') }})
    r"""The current outstanding amount charged for late payment."""
    escrow_balance: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escrow_balance') }})
    r"""Total amount held in escrow to pay taxes and insurance on behalf of the borrower."""
    has_pmi: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_pmi') }})
    r"""Indicates whether the borrower has private mortgage insurance in effect."""
    has_prepayment_penalty: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_prepayment_penalty') }})
    r"""Indicates whether the borrower will pay a penalty for early payoff of mortgage."""
    interest_rate: MortgageInterestRate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interest_rate') }})
    r"""Object containing metadata about the interest rate for the mortgage."""
    last_payment_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_payment_amount') }})
    r"""The amount of the last payment."""
    last_payment_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_payment_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    loan_term: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan_term') }})
    r"""Full duration of mortgage as at origination (e.g. `10 year`)."""
    loan_type_description: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loan_type_description') }})
    r"""Description of the type of loan, for example `conventional`, `fixed`, or `variable`. This field is provided directly from the loan servicer and does not have an enumerated set of possible values."""
    maturity_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maturity_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Original date on which mortgage is due in full. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    next_monthly_payment: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_monthly_payment') }})
    r"""The amount of the next payment."""
    next_payment_due_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_payment_due_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The due date for the next payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    origination_date: Optional[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""
    origination_principal_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origination_principal_amount') }})
    r"""The original principal balance of the mortgage."""
    past_due_amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('past_due_amount') }})
    r"""Amount of loan (principal + interest) past due for payment."""
    property_address: MortgagePropertyAddress = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('property_address') }})
    r"""Object containing fields describing property address."""
    ytd_interest_paid: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ytd_interest_paid') }})
    r"""The year to date (YTD) interest paid."""
    ytd_principal_paid: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ytd_principal_paid') }})
    r"""The YTD principal paid."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

