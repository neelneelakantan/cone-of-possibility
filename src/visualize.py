import matplotlib.pyplot as plt
import numpy as np


def plot_trajectory(trajectory, boundary_fn=None, radius=None, radii=None):
    x = trajectory[:, 0]
    y = trajectory[:, 1]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, linewidth=0.8)

    # Circle boundary (existing)
    if radius is not None:
        theta = np.linspace(0, 2*np.pi, 200)
        plt.plot(radius * np.cos(theta), radius * np.sin(theta), 'r--')

    # Star boundary (new)
    if radii is not None:
        n = len(radii)
        thetas = np.linspace(0, 2*np.pi, n+1)
        rs = np.array(list(radii) + [radii[0]])
        xs = rs * np.cos(thetas)
        ys = rs * np.sin(thetas)
        plt.plot(xs, ys, 'r--')

    plt.axis('equal')
    plt.title("Trajectory")
    plt.show()

def draw_circle_boundary(radius):
    theta = np.linspace(0, 2*np.pi, 300)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    plt.plot(x, y, 'r--', linewidth=1.2)


def draw_polygon_boundary(vertices):
    verts = np.array(vertices + [vertices[0]])  # close the loop
    plt.plot(verts[:,0], verts[:,1], 'r--', linewidth=1.2)


def draw_star_boundary(radii):
    n = len(radii)
    thetas = np.linspace(0, 2*np.pi, n+1)
    rs = np.array(list(radii) + [radii[0]])
    xs = rs * np.cos(thetas)
    ys = rs * np.sin(thetas)
    plt.plot(xs, ys, 'r--', linewidth=1.2)

def draw_arbitrary_boundary(fn, xlim=(-2,2), ylim=(-2,2), resolution=400):
    import numpy as np
    xs = np.linspace(xlim[0], xlim[1], resolution)
    ys = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(xs, ys)
    Z = fn(X, Y)

    plt.contour(X, Y, Z, levels=[0], colors='r', linestyles='--')

import matplotlib.pyplot as plt
import numpy as np

def plot_with_boundary(traj=None, 
                       radius=None, 
                       vertices=None, 
                       radii=None, 
                       fn=None,
                       xlim=(-2,2), 
                       ylim=(-2,2),
                       resolution=400):
    """
    Unified plotter for trajectory + any boundary type.
    Only draws what is provided.
    """

    plt.figure(figsize=(6,6))

    # --- Circle ---
    if radius is not None:
        theta = np.linspace(0, 2*np.pi, 300)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        plt.plot(x, y, 'r--', linewidth=1.2)

    # --- Polygon ---
    if vertices is not None:
        verts = np.array(vertices + [vertices[0]])
        plt.plot(verts[:,0], verts[:,1], 'r--', linewidth=1.2)

    # --- Star ---
    if radii is not None:
        n = len(radii)
        thetas = np.linspace(0, 2*np.pi, n+1)
        rs = np.array(list(radii) + [radii[0]])
        xs = rs * np.cos(thetas)
        ys = rs * np.sin(thetas)
        plt.plot(xs, ys, 'r--', linewidth=1.2)

    # --- Arbitrary function boundary ---
    if fn is not None:
        xs = np.linspace(xlim[0], xlim[1], resolution)
        ys = np.linspace(ylim[0], ylim[1], resolution)
        X, Y = np.meshgrid(xs, ys)
        Z = fn(X, Y)
        plt.contour(X, Y, Z, levels=[0], colors='r', linestyles='--')

    # --- Trajectory ---
    if traj is not None:
        plt.plot(traj[:,0], traj[:,1], linewidth=0.8)

    plt.axis('equal')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.title("Trajectory with Boundary")
    plt.show()
