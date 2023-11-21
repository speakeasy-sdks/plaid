"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .transactionsruledetails import TransactionsRuleDetails
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionsCategoryRule:
    r"""A representation of a transactions category rule."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` )."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier of the rule created"""
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item_id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier of the Item the rule was created for."""
    personal_finance_category: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_finance_category'), 'exclude': lambda f: f is None }})
    r"""Personal finance category unique identifier.

    In the personal finance category taxonomy, this field is represented by the detailed category field.
    """
    rule_details: Optional[TransactionsRuleDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule_details'), 'exclude': lambda f: f is None }})
    r"""A representation of transactions rule details."""
    
