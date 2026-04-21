from src.state import State
from src.drift import gaussian_drift
from src.constraints import circle_boundary
from src.project import project_to_circle
from src.simulate import simulate
from src.visualize import plot_with_boundary

# Unconstrained
state = State([0.1, 0.1])
traj_unconstrained = simulate(
    state,
    drift_fn=lambda: gaussian_drift(2, sigma=0.05),
    boundary_fn=None,
    project_fn=None,
    steps=5000
)

# Constrained
state = State([0.1, 0.1])
traj_constrained = simulate(
    state,
    drift_fn=lambda: gaussian_drift(2, sigma=0.05),
    boundary_fn=lambda s: circle_boundary(s, radius=1.0),
    project_fn=lambda s: project_to_circle(s, radius=1.0),
    steps=5000
)

plot_with_boundary(traj_constrained, radius=1.0)
