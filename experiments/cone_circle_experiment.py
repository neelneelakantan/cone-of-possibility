import numpy as np
import matplotlib.pyplot as plt
from src.state import State
from src.drift import gaussian_drift
from src.constraints import circle_boundary
from src.project import project_to_circle
from src.simulate import simulate
from src.visualize import plot_with_boundary

# Radii over time (wide → narrow)
radii = [1.2, 0.9, 0.6]
colors = ["blue", "green", "orange"]
steps_per_phase = 2000

state = State([0.1, 0.1])
phase_trajs = []

for r in radii:
    traj = simulate(
        state,
        drift_fn=lambda: gaussian_drift(2, sigma=0.05),
        boundary_fn=lambda s, rr=r: circle_boundary(s, rr),
        project_fn=lambda s, rr=r: project_to_circle(s, rr),
        steps=steps_per_phase
    )
    phase_trajs.append(traj)
    state = State(traj[-1])

plt.figure(figsize=(6,6))

# Draw final boundary (tightest)
theta = np.linspace(0, 2*np.pi, 300)
plt.plot(radii[-1] * np.cos(theta), radii[-1] * np.sin(theta), 'r--')

# Plot each phase in its own color
for traj, c in zip(phase_trajs, colors):
    plt.plot(traj[:,0], traj[:,1], color=c, linewidth=0.8)

plt.axis('equal')
plt.title("Cone (Top View) with Color Phases")
plt.show()
