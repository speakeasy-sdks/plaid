"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .proxytype import ProxyType
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RiskCheckDevice:
    r"""Result summary object specifying values for `device` attributes of risk check."""
    ip_proxy_type: Optional[ProxyType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_proxy_type') }})
    r"""An enum indicating whether a network proxy is present and if so what type it is.

    `none_detected` indicates the user is not on a detectable proxy network.

    `tor` indicates the user was using a Tor browser, which sends encrypted traffic on a decentralized network and is somewhat similar to a VPN (Virtual Private Network).

    `vpn` indicates the user is on a VPN (Virtual Private Network)

    `web_proxy` indicates the user is on a web proxy server, which may allow them to conceal information such as their IP address or other identifying information.

    `public_proxy` indicates the user is on a public web proxy server, which is similar to a web proxy but can be shared by multiple users. This may allow multiple users to appear as if they have the same IP address for instance.
    """
    ip_spam_list_count: Optional[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_spam_list_count') }})
    r"""Count of spam lists the IP address is associated with if known."""
    ip_timezone_offset: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_timezone_offset') }})
    r"""UTC offset of the timezone associated with the IP address."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

