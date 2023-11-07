"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditCategory:
    r"""Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such use cases.

    See the [`taxonomy csv file`](https://plaid.com/documents/credit-category-taxonomy.csv) for a full list of credit categories.
    """
    detailed: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailed') }})
    r"""A granular category conveying the transaction's intent. This field can also be used as a unique identifier for the category."""
    primary: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary') }})
    r"""A high level category that communicates the broad category of the transaction."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

