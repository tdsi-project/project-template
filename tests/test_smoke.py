import numpy as np
from src.baseline import baseline
from src.metrics import psnr


def test_baseline_shape():
    x = np.random.default_rng(0).random((32, 32))
    assert baseline(x).shape == x.shape


def test_psnr_identical_is_inf():
    x = np.ones((8, 8))
    assert psnr(x, x) == float("inf")
