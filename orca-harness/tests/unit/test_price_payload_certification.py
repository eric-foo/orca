"""Certification honesty tests for rung-1.5 price-payload extraction.

These pin the loud-failure invariants added after the pre-merge review: an
encoded/uninspectable body, an absent token-list cross-check, or an implausible
amount must REFUSE certification (never a well-formed-but-wrong fake-pass), while
a legitimate Free $0 tier must NOT be false-failed.
"""
from source_capture.price_payload_extraction import (
    ResolvedTier,
    ResolvedTierPrice,
    certify_extraction,
)


def _rtp(token, minor, *, resolved=True):
    return ResolvedTierPrice(
        price_token=token,
        descriptor=None,
        price_header=None,
        label=None,
        amount_minor=minor,
        amount_display=(None if minor is None else str(minor)),
        token_updated_at="2026-06-09",
        resolved=resolved,
    )


def _certify(**overrides):
    kwargs = dict(
        page_block_class="content_unverified",
        page_status=200,
        page_block_signal=None,
        chunk_block_class="content_unverified",
        chunk_status=200,
        chunk_block_signal=None,
        token_list=["chatgpt.plus.2026"],
        prices={"chatgpt.plus.2026": {"usd": 2000}},
        resolved_tiers=[
            ResolvedTier(name="Plus", display_order=1, prices=[_rtp("chatgpt.plus.2026", 2000)])
        ],
        currency="usd",
    )
    kwargs.update(overrides)
    return certify_extraction(**kwargs)


def _failed(verdict):
    return {c.name for c in verdict.checks if not c.passed}


def test_happy_path_certifies():
    v = _certify()
    assert v.certified, _failed(v)


def test_encoded_page_body_refuses_certification():
    v = _certify(page_block_signal="encoded_body_uninspectable")
    assert not v.certified
    assert "page_body_inspectable" in _failed(v)


def test_encoded_prices_chunk_refuses_certification():
    v = _certify(chunk_block_signal="encoded_body_uninspectable")
    assert not v.certified
    assert "prices_chunk_body_inspectable" in _failed(v)


def test_absent_token_list_is_not_a_vacuous_pass():
    v = _certify(token_list=[])
    assert not v.certified
    assert "token_list_consistent_with_prices" in _failed(v)


def test_token_list_not_in_prices_refuses_certification():
    v = _certify(token_list=["chatgpt.plus.2026", "chatgpt.ghost.2026"])
    assert not v.certified
    assert "token_list_consistent_with_prices" in _failed(v)


def test_timestamp_shaped_amount_refuses_certification():
    # a reshape that returns an epoch/timestamp instead of a price minor-unit value
    v = _certify(
        prices={"chatgpt.plus.2026": {"usd": 1_733_000_000}},
        resolved_tiers=[
            ResolvedTier(name="Plus", display_order=1,
                         prices=[_rtp("chatgpt.plus.2026", 1_733_000_000)])
        ],
    )
    assert not v.certified
    assert "resolved_amounts_plausible" in _failed(v)


def test_negative_amount_refuses_certification():
    v = _certify(
        prices={"chatgpt.plus.2026": {"usd": -2000}},
        resolved_tiers=[
            ResolvedTier(name="Plus", display_order=1, prices=[_rtp("chatgpt.plus.2026", -2000)])
        ],
    )
    assert not v.certified
    assert "resolved_amounts_plausible" in _failed(v)


def test_free_zero_tier_still_certifies():
    # Free legitimately resolves to $0 -- the plausibility floor is 0, so a real
    # Free tier must NOT be false-failed by the new amount check.
    v = _certify(
        token_list=["chatgpt.free", "chatgpt.plus.2026"],
        prices={"chatgpt.free": {"usd": 0}, "chatgpt.plus.2026": {"usd": 2000}},
        resolved_tiers=[
            ResolvedTier(name="Free", display_order=0, prices=[_rtp("chatgpt.free", 0)]),
            ResolvedTier(name="Plus", display_order=1, prices=[_rtp("chatgpt.plus.2026", 2000)]),
        ],
    )
    assert v.certified, _failed(v)
