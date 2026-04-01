# Dating Terms Court — Podcast Page Delivery Plan

## Purpose
This plan defines a clear, testable delivery sequence for the remaining Dating Terms Court podcast page backlog.
It focuses on repeatable implementation, visible failure handling, and explicit review checkpoints before release.

## Working Principles
1. **Deterministic behavior:** the same inputs should produce the same results.
2. **No silent failures:** user-facing and internal error states are required.
3. **Human review checkpoints:** subjective decisions (content quality, moderation outcomes, messaging) require reviewer sign-off.
4. **Traceable decisions:** each phase includes explicit validation criteria.

---

## Remaining Backlog and Delivery Sequence

### Phase 1 — Navigation Variant Testing (existing TODO)
**Scope:** Test dossier tabs, Y2K pills, and docket dropdown; collect actionable feedback.

**Implementation steps**
1. Add deterministic variant assignment:
   - User-selected mode persisted per user/session, or
   - Stable hash-based assignment by user ID.
2. Add in-page feedback capture tied to current variant:
   - Ease of use (1–5)
   - Visual appeal (1–5)
   - Speed of finding a case (1–5)
   - Free-text notes
3. Build a results view for comparing variant scores.
4. Export structured results for team review.

**Validation checkpoints**
- Product confirms scoring rubric.
- QA confirms assignment is stable across refreshes.
- QA confirms all feedback submit failures are visible to users.

**Human review required**
- Product + design choose final navigation variant after reviewing collected feedback.

---

### Phase 2 — Social Sharing Buttons
**Scope:** Add case sharing that is predictable and safe for public distribution.

**Implementation steps**
1. Add share actions: copy link, X/Twitter, and platform-agnostic share sheet.
2. Share payload includes only public case fields (term, short summary, public URL).
3. Add fallback behavior if share APIs are unavailable.
4. Instrument share attempts and outcomes.

**Validation checkpoints**
- QA validates generated links per platform.
- QA validates fallback on unsupported browsers.

**Human review required**
- Content/editorial review of share text templates.

---

### Phase 3 — Search and Filter Cases
**Scope:** Improve retrieval speed for users browsing many terms.

**Implementation steps**
1. Add deterministic filters (term type, verdict category, source).
2. Add search with exact and prefix matching.
3. Add explicit empty-state and no-results messaging.
4. Track no-results queries for backlog improvements.

**Validation checkpoints**
- QA verifies ranking/tie-break rules are consistent.
- PM validates top user query flows.

**Human review required**
- Editorial review for synonym mappings.

---

### Phase 4 — Trending Cases
**Scope:** Rank and display cases using transparent logic.

**Implementation steps**
1. Define trending formula (weights + lookback window) in config.
2. Persist trend snapshots with timestamp + formula version.
3. Add “How this is calculated” helper text in UI.

**Validation checkpoints**
- QA verifies reproducible ordering from the same inputs.
- Product verifies formula intent aligns with desired behavior.

**Human review required**
- Product approval for any formula changes.

---

### Phase 5 — Comments / Discussion
**Scope:** Add discussion with clear moderation flow.

**Implementation steps**
1. Add comment states: pending, approved, rejected, escalated.
2. Add moderator reason codes for rejected/escalated outcomes.
3. Keep a moderator action log.
4. Add user notifications for status changes.

**Validation checkpoints**
- QA validates all status transitions and notifications.
- QA validates escalation path and audit log entries.

**Human review required**
- Moderator approval before high-risk comments go public.

---

### Phase 6 — User Profiles
**Scope:** Show each user’s submission history clearly.

**Implementation steps**
1. Add submission timeline with status and timestamps.
2. Show clear reason text for rejected/needs-revision submissions.
3. Add immutable status-history records for traceability.

**Validation checkpoints**
- QA verifies timeline matches source event data.
- PM verifies status language clarity.

**Human review required**
- Admin review path for contested moderation outcomes.

---

### Phase 7 — Thursday Live Stream Integration
**Scope:** Support podcast live sessions with operational controls.

**Implementation steps**
1. Add approved provider embed and pre-stream status checks.
2. Add pre-live checklist (host assigned, moderator assigned, backup link set).
3. Log stream metadata (start/end, host, moderator, stream URL).

**Validation checkpoints**
- Rehearsal run before launch.
- QA confirms degraded-mode messaging if stream is unavailable.

**Human review required**
- Go/no-go launch decision by operations owner.

---

### Phase 8 — Mobile App Version
**Scope:** Extend stable web functionality to mobile.

**Implementation steps**
1. Reuse existing APIs with no business-logic drift.
2. Validate mobile UX for voting, submission, and comments.
3. Implement explicit offline and retry messaging.

**Validation checkpoints**
- QA device matrix testing.
- QA confirms consistent behavior across web and mobile.

**Human review required**
- Release approval by product + QA.

---

## Cross-Phase Controls
- Structured logs for vote, submission, moderation, and share events.
- Dashboard alerts for API errors and moderation queue delays.
- Feature-flagged rollout with rollback checklist per phase.

## Global Definition of Done
A phase is complete only when:
1. Acceptance criteria are met.
2. Failure states are implemented and tested.
3. Relevant logs/metrics are validated.
4. Required human-review checkpoint is completed.
5. Release notes and runbook updates are published.
