from matplotlib import pyplot as plt

from src.state import State
from src.drift import gaussian_drift
from src.constraints import arbitrary_boundary
from src.project import project_to_arbitrary
from src.simulate import simulate
from src.visualize import draw_arbitrary_boundary, plot_with_boundary
import numpy as np

# Example arbitrary boundary: wavy circle
def fn(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r - (1 + 0.3*np.sin(5*theta))

state = State([0.1, 0.1])

traj = simulate(
    state,
    drift_fn=lambda: gaussian_drift(2, sigma=0.05),
    boundary_fn=lambda s: arbitrary_boundary(s, fn),
    project_fn=lambda s: project_to_arbitrary(s, fn),
    steps=5000
)

plot_with_boundary(traj, fn=fn)
