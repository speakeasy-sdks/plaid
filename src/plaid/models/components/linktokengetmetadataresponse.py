"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountfiltersresponse import AccountFiltersResponse
from .countrycode import CountryCode
from .linktokencreateinstitutiondata import LinkTokenCreateInstitutionData
from .products import Products
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenGetMetadataResponse:
    r"""An object specifying the arguments originally provided to the `/link/token/create` call."""
    UNSET='__SPEAKEASY_UNSET__'
    client_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_name') }})
    r"""The `client_name` specified in the `/link/token/create` call."""
    country_codes: List[CountryCode] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_codes') }})
    r"""The `country_codes` specified in the `/link/token/create` call."""
    initial_products: List[Products] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_products') }})
    r"""The `products` specified in the `/link/token/create` call."""
    language: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language') }})
    r"""The `language` specified in the `/link/token/create` call."""
    redirect_uri: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirect_uri') }})
    r"""The `redirect_uri` specified in the `/link/token/create` call."""
    webhook: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook') }})
    r"""The `webhook` specified in the `/link/token/create` call."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    account_filters: Optional[AccountFiltersResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_filters'), 'exclude': lambda f: f is None }})
    r"""The `account_filters` specified in the original call to `/link/token/create`."""
    institution_data: Optional[LinkTokenCreateInstitutionData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_data'), 'exclude': lambda f: f is None }})
    r"""A map containing data used to highlight institutions in Link."""
    

