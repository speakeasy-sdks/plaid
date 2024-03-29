"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .linksessionsuccessmetadataaccount import LinkSessionSuccessMetadataAccount
from .linksessionsuccessmetadatainstitution import LinkSessionSuccessMetadataInstitution
from .linksessionsuccessmetadatatransferstatus import LinkSessionSuccessMetadataTransferStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkSessionSuccessMetadata:
    r"""Displayed once a user has successfully linked their Item."""
    UNSET='__SPEAKEASY_UNSET__'
    accounts: Optional[List[LinkSessionSuccessMetadataAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is None }})
    r"""A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, `accounts` will only include selected accounts."""
    institution: Optional[LinkSessionSuccessMetadataInstitution] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution'), 'exclude': lambda f: f is LinkSessionSuccessMetadata.UNSET }})
    r"""An institution object. If the Item was created via Same-Day micro-deposit verification, will be `null`."""
    link_session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_session_id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier associated with a user's actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround."""
    transfer_status: Optional[LinkSessionSuccessMetadataTransferStatus] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer_status'), 'exclude': lambda f: f is LinkSessionSuccessMetadata.UNSET }})
    r"""The status of a transfer. Returned only when [Transfer UI](/docs/transfer/using-transfer-ui) is implemented.

    - `COMPLETE` – The transfer was completed.
    - `INCOMPLETE` – The transfer could not be completed. For help, see [Troubleshooting transfers](/docs/transfer/using-transfer-ui#troubleshooting-transfers).
    """
    

