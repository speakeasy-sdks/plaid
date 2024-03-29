"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .walletbalance import WalletBalance
from .walletnumbers import WalletNumbers
from .walletstatus import WalletStatus
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Wallet:
    r"""An object representing the e-wallet"""
    UNSET='__SPEAKEASY_UNSET__'
    balance: WalletBalance = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})
    r"""An object representing the e-wallet balance"""
    numbers: WalletNumbers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numbers') }})
    r"""An object representing the e-wallet account numbers"""
    status: WalletStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the wallet.

    `UNKNOWN`: The wallet status is unknown.

    `ACTIVE`: The wallet is active and ready to send money to and receive money from.

    `CLOSED`: The wallet is closed. Any transactions made to or from this wallet will error.
    """
    wallet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_id') }})
    r"""A unique ID identifying the e-wallet"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    recipient_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the recipient that corresponds to the e-wallet account numbers"""
    

