import numpy as np
import scipy.optimize as sp

# Calling a data set
data = np.loadtxt('rv_data_2.csv', delimiter=',', skiprows=1)

# Setting Data Variables
err = data[:, 0]
t = data[:, 1]
vr = data[:, 2]


# Modelling residuals
def res(var, t, vr, err):
    # Setting Variables [K, P, phi]
    K1 = var[0]
    K2 = var[1]
    P1 = var[2]
    P2 = var[3]
    phi1 = var[4]
    phi2 = var[5]

    # Objective Function
    obj = K1 * np.sin(2 * np.pi * t / P1 + phi1) + K2 * np.cos(2 * np.pi * t / P2 + phi2)

    # Computing Residuals
    return (obj - vr)/err


# Guess initial variables
var = [10, 3, 30, 20, 2, 2]

# Optimising
fit = sp.leastsq(res, var, args=(t, vr, err))
print(fit)
