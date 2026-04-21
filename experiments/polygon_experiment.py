from src.state import State
from src.drift import gaussian_drift
from src.constraints import polygon_boundary
from src.project import project_to_polygon
from src.simulate import simulate
from src.visualize import draw_polygon_boundary, plot_with_boundary
import matplotlib.pyplot as plt

# Define a hexagon
vertices = [
    [1.0, 0.0],
    [0.5, 0.87],
    [-0.5, 0.87],
    [-1.0, 0.0],
    [-0.5, -0.87],
    [0.5, -0.87]
]

# Constrained polygon experiment
state = State([0.1, 0.1])
traj = simulate(
    state,
    drift_fn=lambda: gaussian_drift(2, sigma=0.05),
    boundary_fn=lambda s: polygon_boundary(s, vertices),
    project_fn=lambda s: project_to_polygon(s, vertices),
    steps=5000
)

plot_with_boundary(traj, vertices=vertices)
