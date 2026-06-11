```yaml
retrieval_header_version: 1
artifact_role: Future-exploration backlog (non-authorizing, capture-spine level)
scope: >
  Deliberately-deferred, legally-gated capture-spine capabilities surfaced during the
  LinkedIn Discovery & Planning Lane design. Records the idea, why it is OUT of the
  discovery lane, the boundary it must not cross, and the preconditions to revisit it.
use_when:
  - Someone proposes relationship-graph analytics or contact/outreach inside a discovery lane.
  - Scoping a future, separately-authorized lane for either capability.
authority_boundary: retrieval_only
```

# Data Capture Spine — Future Exploration Lanes (v0)

## What this is — and is not

This is a **capture-spine-level backlog of deferred capabilities**, surfaced while
designing the LinkedIn Discovery & Planning Lane. It is **not authorized work, not a
build spec, and not legal advice.** Each item below is **out of scope for every
discovery/planning lane** and may be built only as its **own** lane, after its own
architecture pass, **legal review**, and an explicit bounded execution authorization.

Nothing here changes the current discovery lane's Hard Stops or Non-Claims. The
discovery lane continues to forbid these capabilities; this doc only records *where
they would live if pursued* and *what would have to be true first*.

## Future Exploration A — Relationship-Graph Analytics Lane

**The idea.** Apply data science to follower / connection / commenter relationship
graphs — network analysis, influence mapping, community detection — which is
genuinely useful analytically.

**Why it is OUT of every discovery lane.** Building or retaining these graphs is the
single highest-risk capability surfaced in the LinkedIn design:

- it is squarely against LinkedIn's Terms of Service;
- it is the behavior at the center of the major scraping disputes (e.g. hiQ v.
  LinkedIn, Clearview AI);
- under GDPR/PIPEDA-style regimes it is surveillance-grade processing of individuals
  who never consented and who are mostly **not** public actors;
- it flips the spine's posture from *outside-in public-signal intelligence* to
  *social-graph harvesting*.

**Boundary (hard line).** No discovery/planning lane ever emits, retains, or builds
follower / connection / commenter / relationship / employment / org-chart / contact
graphs. Visible *counts or coarse bands* (and their trend over time) remain allowed
context; the **graph itself** does not.

**Preconditions to revisit.** A separate, explicitly-authorized lane; legal review;
a lawful basis and entitlement/consent model; data-minimization by design; and a
clear statement of who the data subjects are and on what basis they are processed.
Never folded into discovery.

## Future Exploration B — Contact / Outreach Lane

**The idea.** B2B contact and outreach — including the question of whether contact
acquisition is acceptable "because it's B2B."

**The distinction that matters.** *Harvesting* (mass extraction of personal contact
data — emails, phones, private contact routes) is **not** the same as *contacting a
business via its published or consented channels*. The first is the hard-stopped
behavior; the second is a legitimate outreach activity with its own legal basis.

**Why it is OUT of every discovery lane.**

- Discovery is **planning**, not outreach — different stage, different authority.
- Even **B2B** personal contact data is personal data under GDPR; harvesting also
  implicates CAN-SPAM / CASL / ePrivacy and LinkedIn ToS.
- Contact acquisition and outreach are explicitly named Non-Claims / Hard Stops of
  the discovery lane.

**Boundary (hard line).** No discovery/planning lane harvests contacts or performs
outreach. Outreach is a separate lane.

**Preconditions to revisit.** A separate **Outreach Lane**; legal review; a lawful
basis + consent / published-channel model; no harvesting; and explicit authorization.

## Cross-cutting

- Both lanes require **legal review** and a **separate explicit authorization** before
  any build — neither is implied by the discovery lane's existence.
- Neither changes the current discovery lane Hard Stops or Non-Claims.
- Both are **out of scope** for the LinkedIn Discovery & Planning Lane and for the
  capture spine's current build scope.

## Non-claims

This document is **not** an authorization, **not** a build spec, **not** legal advice,
**not** a validation or readiness claim, and confers **no** permission to build,
capture, harvest, or process. It is a forward-looking exploration record only.
