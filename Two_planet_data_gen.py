# Same as one ONE_data_gen.py but the model for RV is different
import numpy as np
import pandas as pd

# Parameters
N = 50
P1, P2 = 32, 23
K1, K2 = np.random.normal(9, 4, 2)
phi1, phi2 = np.random.uniform(0, 2*np.pi, 2)

# Generating time values
t = np.sort(np.random.uniform(0, 100, N))

# Model for ONE planet
vr = K1 * np.sin(2 * np.pi * t / P1 + phi1) + K2 * np.sin(2 * np.pi * t / P2 + phi2)

# Errors
errvel = np.random.normal(2, 0.5, size=len(t))

# Adding Gaussian Noise
noise = 2.2
vel = vr + np.random.normal(0, noise, N)

# Saving to CSV
df = pd.DataFrame({"errvel": errvel, "t": t, "vel": vel})
df.to_csv("rv_data_2.csv", index=False)

print(K1, K2, P1, P2, phi1, phi1)
print("Done")
