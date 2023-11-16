"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .identityverificationstepstatus import IdentityVerificationStepStatus
from .riskcheckbehavior import RiskCheckBehavior
from .riskcheckdevice import RiskCheckDevice
from .riskcheckemail import RiskCheckEmail
from .riskcheckidentityabusesignals import RiskCheckIdentityAbuseSignals
from .riskcheckphone import RiskCheckPhone
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RiskCheckDetails:
    r"""Additional information for the `risk_check` step."""
    behavior: Optional[RiskCheckBehavior] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('behavior') }})
    r"""Result summary object specifying values for `behavior` attributes of risk check, when available."""
    devices: List[RiskCheckDevice] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('devices') }})
    r"""Array of result summary objects specifying values for `device` attributes of risk check."""
    email: Optional[RiskCheckEmail] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Result summary object specifying values for `email` attributes of risk check."""
    identity_abuse_signals: Optional[RiskCheckIdentityAbuseSignals] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identity_abuse_signals') }})
    r"""Result summary object capturing abuse signals related to `identity abuse`, e.g. stolen and synthetic identity fraud."""
    phone: Optional[RiskCheckPhone] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone') }})
    r"""Result summary object specifying values for `phone` attributes of risk check."""
    status: IdentityVerificationStepStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of a step in the identity verification process."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

