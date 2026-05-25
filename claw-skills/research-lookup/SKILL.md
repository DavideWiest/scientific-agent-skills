---
name: research-lookup
description: Use when finding current papers, technical sources, citations, or evidence needed to verify a scientific claim.
---

# Research Lookup

Adapted from K-Dense's upstream `research-lookup` skill to use only tools and
credentials actually available in the current Claw environment.

## Method

1. Define the claim or question, desired source type, date range, and
   inclusion constraints.
2. Search using available browsing/search capabilities. Prefer primary papers,
   official repositories, proceedings, journal pages, or authoritative
   documentation over secondary summaries.
3. For significant claims, open and inspect the primary source rather than
   relying on a search snippet.
4. Record title, authors or institution where useful, publication date,
   persistent identifier or URL, and what the source establishes.
5. Distinguish sourced findings from synthesis or inference.

## Routing

- Use `literature-review` for systematic coverage or state-of-the-art claims.
- Use `research` for a durable synthesized deliverable.
- Do not assume availability of upstream `parallel-cli`, Perplexity,
  OpenRouter, or other paid/API backends; use one only when it is configured
  and appropriate for the user's approved workflow.
