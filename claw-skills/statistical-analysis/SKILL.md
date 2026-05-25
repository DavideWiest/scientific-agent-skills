---
name: statistical-analysis
description: Use when planning or reviewing statistical tests, uncertainty estimates, effect sizes, power, assumptions, or interpretation of quantitative results.
---

# Statistical Analysis

Adapted from K-Dense's upstream `statistical-analysis` skill.

## Workflow

1. Define question, outcome, predictors/groups, design, sampling unit,
   dependence structure, exploratory versus confirmatory status, and practical
   effect of interest.
2. Select analysis appropriate to the design and data, including treatment of
   multiple comparisons, missing data, and repeated measurements.
3. Inspect assumptions and diagnostics; choose robust, nonparametric, or
   transformed alternatives when assumptions materially fail.
4. Report effect sizes and uncertainty alongside significance measures. Do not
   equate statistical significance with practical or scientific importance.
5. Record analysis code, preprocessing, exclusions, seeds where relevant, and
   limitations sufficient for reproduction.

Use installed project libraries when implementing analyses; do not assume an
upstream optional package or script is available.
