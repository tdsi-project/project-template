"""Evaluation metrics. Add the ones relevant to your task."""
import numpy as np


def mse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean((a - b) ** 2))


def psnr(a: np.ndarray, b: np.ndarray, data_range: float = 1.0) -> float:
    err = mse(a, b)
    return float("inf") if err == 0 else float(10 * np.log10(data_range**2 / err))
