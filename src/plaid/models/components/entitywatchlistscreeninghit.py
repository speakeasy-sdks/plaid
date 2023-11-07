"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .entityscreeninghitanalysis import EntityScreeningHitAnalysis
from .entityscreeninghitdata import EntityScreeningHitData
from .entitywatchlistcode import EntityWatchlistCode
from .watchlistscreeninghitstatus import WatchlistScreeningHitStatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityWatchlistScreeningHit:
    r"""Data from a government watchlist that has been attached to the screening."""
    first_active: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_active'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    historical_since: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('historical_since'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""ID of the associated entity screening hit."""
    inactive_since: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inactive_since'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""An ISO8601 formatted timestamp."""
    list_code: EntityWatchlistCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_code') }})
    r"""Shorthand identifier for a specific screening list for entities.
     `AU_CON`: Australia Department of Foreign Affairs and Trade Consolidated List
     `CA_CON`: Government of Canada Consolidated List of Sanctions
     `EU_CON`: European External Action Service Consolidated List
     `IZ_SOE`: State Owned Enterprise List
     `IZ_UNC`: United Nations Consolidated Sanctions
     `IZ_WBK`: World Bank Listing of Ineligible Firms and Individuals
     `US_CAP`: US OFAC Correspondent Account or Payable-Through Account Sanctions
     `US_FSE`: US OFAC Foreign Sanctions Evaders
     `US_MBS`: US Non-SDN Menu-Based Sanctions
     `US_SDN`: US Specially Designated Nationals List 
     `US_SSI`: US OFAC Sectoral Sanctions Identifications
     `US_CMC`: US OFAC Non-SDN Chinese Military-Industrial Complex List
     `US_UVL`: Bureau of Industry and Security Unverified List
     `UK_HMC`: UK HM Treasury Consolidated List
    """
    plaid_uid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_uid') }})
    r"""A universal identifier for a watchlist individual that is stable across searches and updates."""
    review_status: WatchlistScreeningHitStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('review_status') }})
    r"""The current state of review. All watchlist screening hits begin in a `pending_review` state but can be changed by creating a review. When a hit is in the `pending_review` state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as `confirmed` or `dismissed` it will no longer be updated so that the state is as it was when the review was first conducted."""
    source_uid: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_uid') }})
    r"""The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is `null`."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    analysis: Optional[EntityScreeningHitAnalysis] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('analysis'), 'exclude': lambda f: f is None }})
    r"""Analysis information describing why a screening hit matched the provided entity information"""
    data: Optional[EntityScreeningHitData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""Information associated with the entity watchlist hit"""
    

