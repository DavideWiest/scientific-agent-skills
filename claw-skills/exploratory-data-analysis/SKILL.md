---
name: exploratory-data-analysis
description: Use when inspecting a scientific or ML dataset to understand structure, quality, distributions, anomalies, and appropriate next analyses.
---

# Exploratory Data Analysis

Adapted from K-Dense's upstream `exploratory-data-analysis` skill without
assuming its domain-specific scripts or all referenced packages are installed.

## Workflow

1. Identify file format, data provenance, units, splits/groups, collection
   process, and the decision the exploration should inform.
2. Inspect shape/schema, types, missingness, duplicates, invalid values,
   class/group balance, ranges, and representative samples.
3. Examine distributions, correlations or dependencies, outliers, leakage
   risks, preprocessing needs, and relevant subgroup behavior.
4. Use visualizations or summaries appropriate to the data and preserve
   reproducible analysis code for durable conclusions.
5. Report data-quality limitations and proposed next analyses; do not treat
   exploratory patterns as confirmed hypotheses.

For formal tests proceed through `test-hypothesis` or `statistical-analysis`;
for conclusions affecting a research claim use `scientific-critical-thinking`.
