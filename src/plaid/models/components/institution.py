"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .authmetadata import AuthMetadata
from .countrycode import CountryCode
from .institutionstatus import InstitutionStatus
from .paymentinitiationmetadata import PaymentInitiationMetadata
from .products import Products
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Institution:
    r"""Details relating to a specific financial institution"""
    UNSET='__SPEAKEASY_UNSET__'
    country_codes: List[CountryCode] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_codes') }})
    r"""A list of the country codes supported by the institution."""
    institution_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id') }})
    r"""Unique identifier for the institution. Note that the same institution may have multiple records, each with different institution IDs; for example, if the institution has migrated to OAuth, there may be separate `institution_id`s for the OAuth and non-OAuth versions of the institution. Institutions that operate in different countries or with multiple login portals may also have separate `institution_id`s for each country or portal."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The official name of the institution."""
    oauth: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth') }})
    r"""Indicates that the institution has an OAuth login flow. This will be `true` if OAuth is supported for any Items associated with the institution, even if the institution also supports non-OAuth connections."""
    products: List[Products] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products') }})
    r"""A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return `auth` in the product array; institutions that do not list `auth` may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the `auth_metadata` object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/)."""
    routing_numbers: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routing_numbers') }})
    r"""A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    auth_metadata: Optional[AuthMetadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_metadata'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""Metadata that captures information about the Auth features of an institution."""
    dtc_numbers: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dtc_numbers'), 'exclude': lambda f: f is None }})
    r"""A partial list of DTC numbers associated with the institution."""
    logo: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""Base64 encoded representation of the institution's logo, returned as a base64 encoded 152x152 PNG. Not all institutions' logos are available."""
    payment_initiation_metadata: Optional[PaymentInitiationMetadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_initiation_metadata'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests."""
    primary_color: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_color'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""Hexadecimal representation of the primary color used by the institution"""
    status: Optional[InstitutionStatus] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.

    Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment.
    """
    url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is Institution.UNSET }})
    r"""The URL for the institution's website"""
    

