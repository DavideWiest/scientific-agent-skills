---
name: hypothesis-generation
description: Use when turning observations or literature gaps into competing, falsifiable scientific hypotheses and discriminating experiments.
---

# Hypothesis Generation

Adapted from K-Dense's upstream `hypothesis-generation` skill for Claw's
evidence-first workflow.

## Workflow

1. Define the observation or gap, its scope, and what is already known versus
   uncertain.
2. Use `literature-review` or `research` to find existing explanations,
   contradictory evidence, and prior tests.
3. Generate multiple plausible competing hypotheses, including a conservative
   or null explanation when appropriate.
4. For each hypothesis state mechanism, assumptions, falsifier, predicted
   observation, and relevant existing evidence.
5. Rank experiments by how efficiently they distinguish the hypotheses, not
   by how likely they are to yield an attractive result.
6. Hand a selected controlled comparison to `test-hypothesis`; use
   `scientific-critical-thinking` when interpreting evidence.

## Output

Record the observation, competing hypotheses, discriminating predictions,
proposed experiments/controls, prior-work links, and remaining uncertainty.
Figures may be useful for causal structures or mechanisms, but are optional
and should be created only when they improve understanding.
