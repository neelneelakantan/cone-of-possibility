import numpy as np
from src.state import State
from src.drift import gaussian_drift
from src.constraints import star_boundary
from src.project import project_to_star
from src.simulate import simulate
from src.visualize import plot_with_boundary

base_radii = np.array([1.0, 0.6, 1.2, 0.8, 1.4, 0.7, 1.1])
scales = [1.0, 0.8, 0.6]  # wide → narrow
steps_per_phase = 2000

state = State([0.1, 0.1])
all_traj = []

for s in scales:
    radii = (s * base_radii).tolist()
    traj = simulate(
        state,
        drift_fn=lambda: gaussian_drift(2, sigma=0.05),
        boundary_fn=lambda st, rr=radii: star_boundary(st, rr),
        project_fn=lambda st, rr=radii: project_to_star(st, rr),
        steps=steps_per_phase
    )
    all_traj.append(traj)
    state = State(traj[-1])

full_traj = np.vstack(all_traj)

plot_with_boundary(full_traj, radii=(scales[-1] * base_radii).tolist(),
                   xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
