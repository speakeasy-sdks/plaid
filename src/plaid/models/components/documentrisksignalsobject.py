"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .multidocumentrisksignal import MultiDocumentRiskSignal
from .singledocumentrisksignal import SingleDocumentRiskSignal
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocumentRiskSignalsObject:
    r"""Object containing fraud risk data for a set of income documents."""
    account_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""ID of the payroll provider account."""
    multi_document_risk_signals: List[MultiDocumentRiskSignal] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multi_document_risk_signals') }})
    r"""Array of risk signals computed from a set of uploaded documents and the associated documents' metadata"""
    single_document_risk_signals: List[SingleDocumentRiskSignal] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('single_document_risk_signals') }})
    r"""Array of document metadata and associated risk signals per document"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

