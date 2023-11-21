"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .numbersach import NumbersACH
from .numbersbacs import NumbersBACS
from .numberseft import NumbersEFT
from .numbersinternational import NumbersInternational
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthGetNumbers:
    r"""An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty."""
    ach: List[NumbersACH] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ach') }})
    r"""An array of ACH numbers identifying accounts."""
    bacs: List[NumbersBACS] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bacs') }})
    r"""An array of BACS numbers identifying accounts."""
    eft: List[NumbersEFT] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eft') }})
    r"""An array of EFT numbers identifying accounts."""
    international: List[NumbersInternational] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('international') }})
    r"""An array of IBAN numbers identifying accounts."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    
