import numpy as np
import scipy.optimize as sp

# Calling a data set
data = np.loadtxt('rv_data_1.csv', delimiter=',', skiprows=1)

# Setting Data Variables
err = data[:, 0]
t = data[:, 1]
vr = data[:, 2]


# Modelling residuals
def res(var, t, vr, err):
    # Setting Variables [K, P, phi]
    K = var[0]
    P = var[1]
    phi = var[2]

    # Objective Function
    obj = K * np.sin(2 * np.pi / P * t + phi)

    # Computing Residuals
    return (obj - vr) / err


# Guess initial variables
var = [9, 30, np.pi/2]

# Optimising
fit = sp.leastsq(res, var, args=(t, vr, err))
