"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .linktokengetmetadataresponse import LinkTokenGetMetadataResponse
from .linktokengetsessionsresponse import LinkTokenGetSessionsResponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenGetResponse:
    r"""LinkTokenGetResponse defines the response schema for `/link/token/get`"""
    created_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The creation timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    expiration: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The expiration timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    link_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_token') }})
    r"""A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`."""
    metadata: LinkTokenGetMetadataResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    r"""An object specifying the arguments originally provided to the `/link/token/create` call."""
    request_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_id') }})
    r"""A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    link_sessions: Optional[List[LinkTokenGetSessionsResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_sessions'), 'exclude': lambda f: f is None }})
    r"""Information about link sessions created using this `link_token`."""
    

