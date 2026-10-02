"""Classical baseline. Replace with your own method (filtering, wavelets, spectral, ...)."""
import numpy as np
from scipy.ndimage import gaussian_filter


def baseline(x: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Placeholder baseline: Gaussian smoothing."""
    return gaussian_filter(x, sigma=sigma)
