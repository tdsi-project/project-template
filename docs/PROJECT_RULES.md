# Image & Signal Processing: Group Project

**Groups:** 2–3 students · **Topic choice:** [early October] · **Intermediate evaluation:** [date] · **Final evaluation:** [mid-January]
**Dedicated sessions:** 20 × 2 h, plus personal work

---

## 1. Goals

You will take a real image or signal processing problem from a list of topics and work on it like a small research project: understand the problem, implement a baseline, propose and test an improvement, and communicate honestly what worked and what did not. A well-analysed negative result is better than an unexplained good number.

## 2. Deliverables and calendar

| When | Deliverable | Format |
|---|---|---|
| Intermediate | Pitch | 5 min + 2 min questions, ≤ 5 slides |
| Intermediate | Report | 2 pages: problem, related work, planned method, baseline results |
| Final | GitHub repository | Code, README, environment file, demo notebook |
| Final | Report | 4 pages, extending the intermediate report (not a new document) |
| Final | Presentation + live demo | [15] min + [10] min individual questions |
| Final | Individual statement | ½ page per student: your contribution and your use of AI tools |

**Repository requirements**
- `README.md`: problem, method, how to run, main results, group members.
- `requirements.txt` or `environment.yml`, with pinned versions for key libraries.
- A demo notebook that runs end to end in **under 10 minutes** on a free Colab session or a CPU. Provide cached results or pre-trained weights if needed.
- Use branches or pull requests; commits should be regular throughout the project, not a single upload at the end. Each member must have visible commits.
- Include a `data/README` explaining how to obtain the dataset. Do not commit large data files.

## 3. Mandatory scientific content

1. **A classical baseline first** (filtering, wavelets, Fourier/spectral methods, optimisation-based methods, etc.), before any deep learning.
2. **Quantitative evaluation** with metrics appropriate to the task, on a held-out test set.
3. **At least one ablation or sensitivity study** (a parameter, a component, a noise level, etc.).
4. **Error analysis**: show and discuss failure cases.
5. **Fair comparison**: same data, same metrics, and comparable tuning effort for all methods.

Using a pre-trained model or an existing library is fine, provided you state clearly what you implemented yourselves and what you reused.

## 4. Use of AI tools

AI assistants (code or text) are **allowed** under these conditions:
- You must **disclose** your use in the individual statement: which tools, for which tasks, and what you verified or modified.
- You are responsible for everything you submit. Any student must be able to explain any line of code or any equation in the project, during the final questions.
- Do not present AI-generated text as your own analysis. The discussion of results must reflect what you actually observed.
- Cite external code, papers, and datasets.

Undisclosed use, or inability to explain submitted work, is handled as a lack of mastery of the project in the individual grade, and as academic misconduct if there is evidence of concealment. [Adapt to your institution's policy.]

## 5. Compute and environmental frugality

- Most topics can be completed on CPU or on a single free-tier GPU. **GPU use is optional.** A lightweight or classical approach is a legitimate choice.
- Available resources: [university cluster / lab machines], Google Colab, Kaggle Notebooks, [others].
- **Budget:** at most [10] GPU-hours per group. Beyond that, justify it in your report.
- Prefer fine-tuning or pre-trained features to training from scratch. Use small or downscaled datasets, early stopping, fixed seeds, and cached results. Avoid large grid searches.
- **Report your footprint** in a short paragraph in the final report: hardware, total runtime, estimated energy and CO₂ (for example with CodeCarbon, or ecologits for LLM API usage), and what you did to reduce it. Estimates are approximate and that is acceptable; state their limits (water use, for instance, depends on the data centre and is not measured by these tools).
- You are not penalised for needing more compute, only for not measuring or not justifying it.

## 6. Grading

**Overall weighting:** intermediate evaluation [25]% · final evaluation [75]%.
**Group vs individual:** the group grade is adjusted per student (±[2] points) based on the individual questions, the statement, and the commit history.

### Intermediate evaluation (100 points)

| Criterion | Points | What we look for |
|---|---|---|
| Problem understanding | 25 | Clear formulation, stakes, data and metrics identified |
| Related work and chosen approach | 25 | Relevant references, justified method choice |
| Baseline | 30 | Working classical baseline with first quantitative results |
| Pitch and report clarity | 20 | Timing, structure, readable figures, plan for the remaining weeks |

### Final evaluation (100 points)

| Criterion | Points | What we look for |
|---|---|---|
| Method and understanding | 25 | Correct, justified choices; mathematical understanding of the methods used |
| Experimental rigor | 25 | Baselines, appropriate metrics, ablation, fair comparison, error analysis |
| Repository and reproducibility | 15 | Clean README, working environment, demo runs within time, commit history |
| Communication | 15 | Report (structure, figures, concision) and talk (clarity, timing, demo) |
| Individual understanding | 10 | Answers to individual questions; coherence with the individual statement |
| Sustainability and transparency | 10 | Footprint estimate, frugal choices, honest AI-use disclosure |

### Scoring levels (applies to each criterion)

- **Excellent (≥ 85%)**: complete, justified, goes beyond requirements, insightful discussion.
- **Good (65–85%)**: complete and correct, limited depth in analysis or justification.
- **Fair (40–65%)**: working but incomplete, or results reported without explanation.
- **Insufficient (< 40%)**: missing, incorrect, or not reproducible.

## 7. Live demo protocol

During the final session, the instructor may provide a new image or signal. You will run your notebook on it and may be asked to change a parameter and explain the effect. Prepare for this: test your notebook from a clean environment before the session.

## 8. Practical rules

- Late submissions: [–X points per day].
- Group problems (conflict, absence): contact the instructor early, not at the end.
- Plagiarism and unreferenced reuse of code or text are treated according to [institution policy].
