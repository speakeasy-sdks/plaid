"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entityscreeninghiturls import EntityScreeningHitUrls
from .matchsummary import MatchSummary
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityScreeningHitUrlsItems:
    r"""Analyzed URLs for the associated hit"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    analysis: Optional[MatchSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('analysis'), 'exclude': lambda f: f is None }})
    r"""Summary object reflecting the match result of the associated data"""
    data: Optional[EntityScreeningHitUrls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""URLs associated with the entity screening hit"""
    

