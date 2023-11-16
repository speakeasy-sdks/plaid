"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .linkdeliverydeliverymethod import LinkDeliveryDeliveryMethod
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkDeliveryCommunicationMethod:
    r"""The communication method containing both the type and address to send the URL."""
    address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""The phone number / email address that Hosted Link sessions are delivered to. Phone numbers must be in E.164 format."""
    method: Optional[LinkDeliveryDeliveryMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method'), 'exclude': lambda f: f is None }})
    r"""The delivery method to be used to deliver the Hosted Link session URL.

    `SMS`: The URL will be delivered through SMS

    `EMAIL`: The URL will be delivered through email
    """
    

