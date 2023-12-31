"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DashboardUserStatus(str, Enum):
    r"""The current status of the user."""
    INVITED = 'invited'
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
