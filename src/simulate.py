import numpy as np

def simulate(
    state,
    drift_fn,
    boundary_fn=None,
    project_fn=None,
    steps=1000
):
    """
    Core simulation loop.
    Returns trajectory as a list of states.
    """

    trajectory = [state.copy()]

    for _ in range(steps):
        delta = drift_fn()
        state.update(delta)

        if boundary_fn is not None:
            if boundary_fn(state.value) > 0:  # outside
                corrected = project_fn(state.value)
                state.value = corrected

        trajectory.append(state.copy())

    return np.array(trajectory)
