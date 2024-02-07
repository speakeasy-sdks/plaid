"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .assetreportfreddie import AssetReportFreddie
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetReportFreddieGetResponse:
    r"""AssetReportFreddieGetResponse defines the response schema for `/asset_report/get`"""
    deal: AssetReportFreddie = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DEAL') }})
    r"""An object representing an Asset Report with Freddie Mac schema."""
    schema_version: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SchemaVersion') }})
    r"""The Verification Of Assets (aka VOA or Freddie Mac Schema) schema version."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

