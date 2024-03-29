"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .selfieanalysisdocumentcomparison import SelfieAnalysisDocumentComparison
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SelfieAnalysis:
    r"""High level descriptions of how the associated selfie was processed. If a selfie fails verification, the details in the `analysis` object should help clarify why the selfie was rejected."""
    UNSET='__SPEAKEASY_UNSET__'
    document_comparison: SelfieAnalysisDocumentComparison = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_comparison') }})
    r"""Information about the comparison between the selfie and the document (if documentary verification also ran)."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

