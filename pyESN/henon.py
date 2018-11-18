
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


def henon_step(x, y, a=1.4, b=0.3):
    x_dot = a + b * y - x*x
    y_dot = x
    return x_dot, y_dot

def henon():
	dt = 0.01
	stepCnt = 100000

	# Need one more for the initial values
	xs = np.empty((stepCnt + 1,))
	ys = np.empty((stepCnt + 1,))

	# Setting initial values
	xs[0], ys[0] = (1., 1.,)

	# Stepping through "time".
	for i in range(stepCnt):
	    # Derivatives of the X, Y, Z state
	    x_dot, y_dot, = henon_step(xs[i], ys[i])
	    xs[i + 1] = x_dot
	    ys[i + 1] = y_dot

	return xs, ys