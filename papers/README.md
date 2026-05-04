# Paper Pool

This directory contains the retained paper pool and screening-decision log for the LLM-MAS RL survey artifact.

## Files

- `papers.csv`: 84 retained entries with taxonomy tags.
- `excluded.csv`: 32 screened-but-excluded records with decision notes.
- `papers.bib`: BibTeX database used by the manuscript.

## Schema

`papers.csv` uses one header row and the following fields:

```text
key,title,first_author,affiliation,year,arxiv_id,venue,url,
category,is_rl,reward_type,credit_granularity,orchestration_form,
scenario,is_core,one_liner,verified,notes
```

The corpus is curated and taxonomy-oriented. It is not a full PRISMA-style systematic-review export. The visible paper list in the top-level README is generated from this CSV with `python scripts/generate_readme_papers.py`.
