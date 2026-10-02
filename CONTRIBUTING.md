# Working rules for the group

- **Never push large files** (datasets, model weights, > 5 MB). Use download scripts (`data/README.md`) or external storage.
- **Never commit secrets** (API keys, tokens). Use environment variables.
- **Branches:** one branch per feature or experiment, named `firstname/short-topic`. Merge into `main` through a pull request.
- **Commits:** small and frequent, with a message saying what and why ("add Wiener baseline", not "update").
- **Everyone commits.** Each member must have visible commits (code, experiments, or report sources).
- **Seeds:** fix random seeds so that results are reproducible.
- **Notebooks:** clear heavy outputs before committing, except figures needed in the demo.
- **Tags (submission):**
  - `v0.5-intermediate` for the intermediate evaluation
  - `v1.0-final` for the final evaluation
  What is graded is the content of the tag at the deadline.
