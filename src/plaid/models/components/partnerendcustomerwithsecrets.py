"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .partnerendcustomersecrets import PartnerEndCustomerSecrets
from .partnerendcustomerstatus import PartnerEndCustomerStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PartnerEndCustomerWithSecrets:
    r"""The details for the newly created end customer, including secrets for non-Production environments."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name'), 'exclude': lambda f: f is None }})
    secrets: Optional[PartnerEndCustomerSecrets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secrets'), 'exclude': lambda f: f is None }})
    r"""The secrets for the newly created end customer in non-Production environments."""
    status: Optional[PartnerEndCustomerStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the given end customer.

    `UNDER_REVIEW`: The end customer has been created and enabled in the non-Production environments. The end customer must be manually reviewed by the Plaid team before it can be enabled in production, at which point its status will automatically transition to `PENDING_ENABLEMENT` or `DENIED`.

    `PENDING_ENABLEMENT`: The end customer is ready to be enabled in the Production environment. Call the `/partner/customer/enable` endpoint to enable the end customer in Production.

    `ACTIVE`: The end customer has been enabled in all environments.

    `DENIED`: The end customer has been created and enabled in the non-Production environments, but it did not pass review by the Plaid team and therefore cannot be enabled in the Production environment. Talk to your Account Manager for more information.
    """
    

