
# Plot of the Lorenz Attractor based on Edward Lorenz's 1963 "Deterministic
# Nonperiodic Flow" publication.
# http://journals.ametsoc.org/doi/abs/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2
#
# Note: Because this is a simple non-linear ODE, it would be more easily
#       done using SciPy's ode solver, but this approach depends only
#       upon NumPy.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz_step(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def lorenz():
	dt = 0.01
	stepCnt = 100000

	# Need one more for the initial values
	xs = np.empty((stepCnt + 1,))
	ys = np.empty((stepCnt + 1,))
	zs = np.empty((stepCnt + 1,))

	# Setting initial values
	xs[0], ys[0], zs[0] = (0., 1., 1.05)

	# Stepping through "time".
	for i in range(stepCnt):
	    # Derivatives of the X, Y, Z state`
	    x_dot, y_dot, z_dot = lorenz_step(xs[i], ys[i], zs[i])
	    xs[i + 1] = xs[i] + (x_dot * dt)
	    ys[i + 1] = ys[i] + (y_dot * dt)
	    zs[i + 1] = zs[i] + (z_dot * dt)

	return xs, ys, zs