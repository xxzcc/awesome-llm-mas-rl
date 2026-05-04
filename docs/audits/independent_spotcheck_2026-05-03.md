# Independent Spot-Check Audit

Date: 2026-05-03

This is a limited independent spot-check of the retained-entry taxonomy.
It is not a blinded multi-annotator agreement study: the annotator had
already seen the original CSV and manuscript framing.  The audit should
therefore be described as an adjudication-style reliability check, not as
Cohen's kappa, Krippendorff's alpha, or PRISMA-quality duplicate coding.

## Scope

The spot-check covers 32 retained rows:

- all claim-critical sparse-credit rows listed in `docs/claim_ledger.md`;
- industrial deployment/training-shape rows used in the scale-gap argument;
- representative RL-method rows across shared, hybrid, role, process,
  debate, and orchestration reward families;
- representative benchmark, survey, and classical-MARL background rows.

The checked fields are:

- `category`
- `is_rl`
- `reward_type`
- `credit_granularity`
- `orchestration_form`

The audit also records whether the row contains a strict explicit credit
mechanism, which is narrower than the paper's broad `credit_granularity`
field.

## Result

Under the paper's current broad tagging rule, the spot-check mostly
supports the retained labels.  The main disagreement is `halo`: I would
tag the broad credit/design signal as `orchestrator` rather than `role`,
because the salient object is hierarchical orchestration/search rather
than a role-specific reward or credit unit.

The more important finding is definitional rather than numerical:
`credit_granularity` is currently broader than "explicit credit
assignment."  It includes reward-bearing objects and design signals.  That
is defensible for a mapping review, but the manuscript must keep saying
so.  If a reviewer reads the field as "strict explicit credit estimator,"
then the sparse-credit counts become narrower:

- message-level: `c3` is strict counterfactual message credit;
  `debate-as-reward` is a message-level reward signal, not counterfactual
  credit.
- orchestrator-level: `puppeteer`, `paramanager`, `kimi-k2-5`, and
  `owl2025` are strict or near-strict trained-orchestrator signals in this
  spot-check; `hera`, `agentspawn`, and `mas-zero2025` are broad
  orchestration design/evolution signals rather than disclosed RL credit.

## Submission Implication

The paper should not claim full multi-annotator reliability.  A truthful
sentence would be:

> A second-pass spot check by an independent reader covered 32 retained
> rows, including all sparse-credit and industrial anchor rows.  The check
> found high agreement under our broad controlled-field definitions, with
> one credit-granularity disagreement (`HALO`) and several rows where the
> distinction between broad design signal and strict explicit credit should
> remain visible.  We therefore report the audit as a reliability
> spot-check, not as a multi-annotator agreement statistic.

For the main paper, the stronger and safer fix is to add a short
"Reliability and auditability" paragraph explaining that all count claims
are retained-pool claims, that `credit_granularity` is a broad field, and
that strict explicit-credit claims are separately qualified in the claim
ledger.

