import numpy as np

def circle_boundary(state, radius=1.0):
    """
    Boundary function for a circle.
    <= 0 means inside, > 0 means outside.
    """
    x, y = state
    return (x**2 + y**2) - radius**2

def polygon_boundary(state, vertices):
    """
    Boundary function for a polygon.
    Uses the winding number / half-space method.
    <= 0 means inside, > 0 means outside.
    """
    x, y = state
    inside = True

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        # Compute cross product to check which side of the edge we're on
        cross = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        if cross > 0:  # outside for CCW polygons
            inside = False
            break

    return 0 if inside else 1


def star_boundary(state, radii):
    """
    Star-shaped boundary.
    radii: list of radial limits for each angle segment.
    <= 0 means inside, > 0 means outside.
    """
    x, y = state
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)

    # Normalize angle to [0, 2π)
    if theta < 0:
        theta += 2 * np.pi

    # Determine which segment this angle falls into
    n = len(radii)
    segment = int((theta / (2 * np.pi)) * n)

    # Allowed radius for this direction
    r_max = radii[segment]

    return r - r_max

def arbitrary_boundary(state, fn):
    """
    Arbitrary boundary defined by a user-provided function fn(x, y).
    <= 0 means inside, > 0 means outside.
    """
    x, y = state
    return fn(x, y)


