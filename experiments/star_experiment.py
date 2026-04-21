from src.state import State
from src.drift import gaussian_drift
from src.constraints import star_boundary
from src.project import project_to_star
from src.simulate import simulate
from src.visualize import draw_star_boundary, plot_with_boundary

# Define a 7-point star with uneven radii (multi-metric constraints)
radii = [1.0, 0.6, 1.2, 0.8, 1.4, 0.7, 1.1]

state = State([0.1, 0.1])

traj = simulate(
    state,
    drift_fn=lambda: gaussian_drift(2, sigma=0.05),
    boundary_fn=lambda s: star_boundary(s, radii),
    project_fn=lambda s: project_to_star(s, radii),
    steps=5000
)

plot_with_boundary(traj, radii=radii)

