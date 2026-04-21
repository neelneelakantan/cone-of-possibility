import numpy as np
from src.constraints import circle_boundary, polygon_boundary

def project_to_circle(state, radius=1.0):
    """Project a point back onto the circle boundary."""
    x, y = state
    norm = np.sqrt(x**2 + y**2)
    if norm == 0:
        return np.array([radius, 0.0])
    return radius * np.array([x / norm, y / norm])


def project_to_polygon(state, vertices):
    """
    Simple projection: move the point toward the polygon centroid
    until it is inside.
    """
    centroid = np.mean(vertices, axis=0)
    direction = centroid - state
    direction = direction / np.linalg.norm(direction)

    # Step inward until inside
    new_state = state.copy()
    for _ in range(100):
        if polygon_boundary(new_state, vertices) <= 0:
            break
        new_state += 0.01 * direction

    return new_state


def project_to_star(state, radii):
    """
    Project a point back onto the star boundary.
    """
    x, y = state
    theta = np.arctan2(y, x)
    if theta < 0:
        theta += 2 * np.pi

    n = len(radii)
    segment = int((theta / (2 * np.pi)) * n)
    r_max = radii[segment]

    # Project to boundary
    return r_max * np.array([np.cos(theta), np.sin(theta)])

def project_to_arbitrary(state, fn, step=0.01, max_iter=500):
    """
    Project a point back inside an arbitrary boundary by moving toward the origin.
    """
    import numpy as np

    new_state = np.array(state, dtype=float)

    for _ in range(max_iter):
        if fn(new_state[0], new_state[1]) <= 0:
            break
        direction = -new_state
        direction /= np.linalg.norm(direction)
        new_state += step * direction

    return new_state



