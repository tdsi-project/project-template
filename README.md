# [Project title]

**Course:** Image & Signal Processing Option, INSA Lyon, [202X] 

**Group:** [XX]

**Members:** [Name 1, Name 2, Name 3]

**Instructor:** [name]

**Rules and grading:** see the [`info`](../info/README.md) repository

## 1. Problem
[2–4 sentences: what task, why it matters, which data, which metrics.]

## 2. Methods
- **Classical baseline:** [method, reference]
- **Proposed method:** [method, reference]
- **What we implemented ourselves vs. reused:** [be explicit]

## 3. Results
[Main table or figure, with the metric(s) and the test set. Link to the report for details.]

| Method | Metric 1 | Metric 2 | Runtime |
|---|---|---|---|
| Baseline | | | |
| Proposed | | | |

## 4. How to run

```bash
# Option A: pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Option B: conda
conda env create -f environment.yml && conda activate isp-project
```

Data: see [`data/README.md`](data/README.md).

Demo: open `notebooks/demo.ipynb` (runs in < 10 min on CPU or free Colab).

Colab: [add an "Open in Colab" badge once the repo is pushed.]

## 5. Repository structure
```
src/          reusable code (baseline, methods, metrics)
notebooks/    demo.ipynb (final demo) and exploration notebooks
data/         download instructions only (no large files in Git)
report/       report sources and PDFs (intermediate, final)
docs/         project rules, individual statements, footprint
tests/        small sanity tests (optional but encouraged)
```

## 6. Environmental footprint
See [`docs/footprint.md`](docs/footprint.md).

## 7. Use of AI tools
See the individual statements in [`docs/ai_usage.md`](docs/ai_usage.md).

## 8. References
[Papers, datasets, code you reused.]
