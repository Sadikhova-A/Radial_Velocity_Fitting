import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from One_planet_fitting import fit

# Loading Data Set
data = pd.read_csv('rv_data_1.csv')

# Periods in the data
periods = [25]

# Set Variables
time = np.array(data.t)
vr_err = np.array(data.errvel)
vr = np.array(data.vel)

# Plotting Noisy Data
plt.errorbar(time, vr, yerr=vr_err, fmt='.k')
plt.xlabel('Time (days)')
plt.ylabel('Radial_Velocity ($ms^{-1}$)')

# Importing variables from least squares
K = fit[0][0]
P = fit[0][1]
phi = fit[0][2]

# Fitting a smooth graph
x = np.linspace(0, 100, 1000)
plt.plot(x, K * np.sin(2 * np.pi / P * x + phi), color='deeppink')
plt.show()
