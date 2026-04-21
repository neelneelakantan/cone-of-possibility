import numpy as np

def gaussian_drift(dim, sigma=0.1):
    """Random Gaussian drift in n dimensions."""
    return np.random.normal(0, sigma, size=dim)
