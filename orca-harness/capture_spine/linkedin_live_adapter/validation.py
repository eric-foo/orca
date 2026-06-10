"""LinkedIn live-adapter -- slice 3a validators.

Translate the accepted live-layer ADR's slice-3a predicates into raising
validators (``LinkedInLaneError``): every negative is a raise, so a test proves
the gate fails bad input rather than passing hollow. The generic fail-closed
primitives (forbidden-output-field walk, key allowlist, required-field check,
NEGATED non_claims category check) are IMPORTED from
``linkedin_lane.shared_validation`` -- the single source of truth -- not
re-implemented.

The load-bearing predicates (ADR refinement B / slice 3a) are enforced here, NOT
carried as enum labels: owner-presence is ATTESTED (a bool that must be True + a
stated check method), entitlement-gate bypass is FORBIDDEN (must be False),
execution is NOT authorized (no-runtime contract record, must be False), the live
mode is one of the two attended modes, and the autonomous attended mode must
carry the POC-risk flag (iff).
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import fields
from typing import Any

from capture_spine.linkedin_lane.shared_validation import (
    assert_no_forbidden_output_fields,
    fail as _fail,
    reject_unknown_keys as _reject_unknown_keys,
    require_fields as _require,
    validate_non_claims_categories as _validate_non_claims,
)
from capture_spine.linkedin_live_adapter.models import (
    LINKEDIN_LIVE_ACCESS_ENVELOPE_SCHEMA_VERSION,
    LiveAccessEnvelope,
    LiveAccessMode,
)


# Fail-closed top-level allowlist, derived from the dataclass so it tracks the
# schema with zero drift and rejects aliased banned keys wholesale.
_ALLOWED_LIVE_ACCESS_ENVELOPE_KEYS = frozenset(f.name for f in fields(LiveAccessEnvelope))
_ALLOWED_LIVE_ACCESS_MODES = frozenset(v.value for v in LiveAccessMode)
# The autonomous (vs purely manual) attended mode carries the POC-risk posture.
_POC_RISK_LIVE_ACCESS_MODE_VALUES = frozenset(
    {LiveAccessMode.OWNER_PRESENT_ATTENDED_AUTOMATION.value}
)

# Required descriptive (str/enum) fields -- present and non-empty. The boolean
# predicates (presence/bypass/execution) are checked separately below.
_REQUIRED_LIVE_ACCESS_ENVELOPE_FIELDS: tuple[str, ...] = (
    "live_access_id",
    "run_id",
    "live_access_mode",
    "source_policy_posture",
    "stop_condition",
    "attended_presence_check_method",
)


def validate_live_access_envelope(envelope: Mapping[str, Any]) -> None:
    assert_no_forbidden_output_fields(envelope)
    _reject_unknown_keys(envelope, _ALLOWED_LIVE_ACCESS_ENVELOPE_KEYS, "live_access_envelope")
    _require(envelope, _REQUIRED_LIVE_ACCESS_ENVELOPE_FIELDS, "live_access_envelope")
    if envelope.get("schema_version") != LINKEDIN_LIVE_ACCESS_ENVELOPE_SCHEMA_VERSION:
        _fail(
            "invalid_schema_version",
            f"live access envelope schema_version must be {LINKEDIN_LIVE_ACCESS_ENVELOPE_SCHEMA_VERSION}",
        )
    if envelope.get("live_access_mode") not in _ALLOWED_LIVE_ACCESS_MODES:
        _fail(
            "invalid_live_access_mode",
            "live_access_mode must be an attended mode "
            "(attended_manual / owner_present_attended_automation); no unattended mode",
        )
    # Presence is an ATTESTED predicate, not a label: the bool must be True
    # (the required check-method backs it via _require above).
    if envelope.get("owner_presence_attested") is not True:
        _fail(
            "presence_not_attested",
            "owner_presence_attested must be True (a live access run requires confirmed owner presence)",
        )
    # No entitlement-gate bypass (hard stop) -- enforced as a predicate, not only declared.
    if envelope.get("entitlement_gate_bypass") is not False:
        _fail(
            "entitlement_gate_bypass_forbidden",
            "entitlement_gate_bypass must be False (no circumventing login walls, caps, or paid tiers)",
        )
    # No runtime in the contract slice: execution must not be authorized here.
    if envelope.get("execution_authorized") is not False:
        _fail(
            "execution_authorization_forbidden",
            "execution_authorized must be False (this is a no-runtime contract record, not a live runner)",
        )
    caps = envelope.get("caps")
    if not isinstance(caps, Mapping) or not caps:
        _fail("missing_caps", "caps are required (a live access run must declare its caps)")
    # Consistency (iff, per ADR §8): the POC-risk flag is True EXACTLY for the
    # autonomous attended mode -- enforced both ways, so the flag cannot
    # over-attest POC-risk on a non-POC (manual) mode.
    is_poc_mode = envelope.get("live_access_mode") in _POC_RISK_LIVE_ACCESS_MODE_VALUES
    poc_flag_set = envelope.get("optional_poc_risk_mode") is True
    if is_poc_mode and not poc_flag_set:
        _fail(
            "poc_risk_mode_not_attested",
            "owner_present_attended_automation is a POC-risk mode; optional_poc_risk_mode must be True",
        )
    if poc_flag_set and not is_poc_mode:
        _fail(
            "poc_risk_mode_overattested",
            "optional_poc_risk_mode=True is valid only for owner_present_attended_automation "
            "(no over-attesting POC-risk on a non-POC mode)",
        )
    _validate_non_claims(envelope.get("non_claims"), "live_access_envelope")
