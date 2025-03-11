import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy.printing.pretty.pretty_symbology import line_width

from TWO_planet_fitting import fit

# Loading Data Set
data = pd.read_csv('rv_data_2.csv')

# Set Variables
time = np.array(data.t)
vr_err = np.array(data.errvel)
vr = np.array(data.vel)

# Plotting Noisy Data
plt.errorbar(time, vr, yerr=vr_err, fmt='.k')
plt.xlabel('Time (days)')
plt.ylabel('Radial_Velocity ($ms^{-1}$)')

# Importing variables from least squares
K1 = fit[0][0]
K2 = fit[0][1]
P1 = fit[0][2]
P2 = fit[0][3]
phi1 = fit[0][4]
phi2 = fit[0][5]

# Fitting a smooth graph
x = np.linspace(0, 100, 1000)
plt.plot(x, K1 * np.sin(2 * np.pi * x / P1 + phi1) + K2 * np.cos(2 * np.pi * x / P2 + phi2), color='deeppink', linewidth=2, label='RV Fit')
plt.plot(x, K1 * np.sin(2 * np.pi * x / P1 + phi1), '--',  color='midnightblue', label="Planet 1")
plt.plot(x, K2 * np.cos(2 * np.pi * x / P2 + phi2), '--',  color='g', label='Planet 2')
plt.legend()
plt.show()
