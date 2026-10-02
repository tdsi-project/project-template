# Environmental footprint

Fill in at the end of the project (and keep this updated as you go).

| Item | Value |
|---|---|
| Hardware (CPU / GPU model, location if known) | |
| Total runtime (CPU-hours / GPU-hours) | |
| Estimated energy (kWh) and CO2e (kg) | |
| Tool used (e.g. CodeCarbon, ecologits) | |
| LLM / API usage (tool, rough volume) | |

**What we did to reduce it:** [baseline first, pretrained models, downscaled data, early stopping, cached features, ...]

**Limits of the estimate:** [tool assumptions, water use not measured, embodied emissions not included, ...]

Minimal CodeCarbon usage:

```python
from codecarbon import EmissionsTracker
tracker = EmissionsTracker(project_name="isp-project", output_dir=".")
tracker.start()
# ... run experiment ...
emissions = tracker.stop()   # kg CO2e
```
