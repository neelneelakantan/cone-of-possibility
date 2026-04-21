import numpy as np

class State:
    """Represents a point in n-dimensional space."""

    def __init__(self, initial):
        self.value = np.array(initial, dtype=float)

    def update(self, delta):
        """Apply a drift or correction update."""
        self.value = self.value + delta

    def copy(self):
        return np.copy(self.value)
