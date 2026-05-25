---
name: peer-review
description: Use when formally reviewing a scientific manuscript, preprint, grant proposal, or research artifact for rigor and constructive feedback.
---

# Peer Review

Adapted from K-Dense's upstream `peer-review` skill without mandatory visual
asset generation.

## Review Sequence

1. Summarize the question, claimed contribution, methods, and main findings.
2. Assess significance and novelty against relevant literature when the claim
   depends on it.
3. Review methodology: controls, sampling/splits, implementation fidelity,
   statistics, reproducibility, ethics where applicable, and reporting
   standards relevant to the study type.
4. Review results and claims: effect sizes/uncertainty, negative results,
   robustness, alternative explanations, and overclaiming.
5. Separate major issues, minor issues, and optional improvements; make each
   point actionable and ground it in a location or evidence.
6. State an overall recommendation only after the reasons are clear.

## Computational/ML Additions

- Check code/data availability, configurations, baselines, tuning fairness,
  leakage, seeds, compute comparability, and whether metrics establish the
  stated claim.
- Use `scientific-critical-thinking` for a focused validity assessment and
  `literature-review` when prior-work coverage or novelty must be checked.
