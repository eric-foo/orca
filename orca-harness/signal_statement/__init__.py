"""Signal Statement Record (v0) -- the second derived-record kind: statement.

Parallel to the ECR integrity postures (``ecr/``); see
``docs/product/signal_statement/core_spine_v0_signal_statement_record_architecture_v0.md``.
Data model + the v0 carry-or-residualize deriver. No persistence, no
EvidenceUnit binding.
"""
from __future__ import annotations

from signal_statement.models import (
    SIGNAL_STATEMENT_MANIFEST_VERSION,
    StatementReferences,
    DecisionRelevance,
    Delta,
    FamilyDetailBase,
    Reaction,
    SignalStatementRecord,
    SignalEventTimeField,
    SignalEventTimeReference,
    SignalEventTimeStatus,
    SignalFamily,
)
from signal_statement.deriver import derive_signal_statement

__all__ = [
    "derive_signal_statement",
    "SIGNAL_STATEMENT_MANIFEST_VERSION",
    "StatementReferences",
    "DecisionRelevance",
    "Delta",
    "FamilyDetailBase",
    "Reaction",
    "SignalStatementRecord",
    "SignalEventTimeField",
    "SignalEventTimeReference",
    "SignalEventTimeStatus",
    "SignalFamily",
]
