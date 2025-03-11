import numpy as np
import pandas as pd

# Parameters
N = 50
P1 = 25
K1 = np.random.normal(9, 4)
phi1 = np.random.uniform(0, 2*np.pi)

# Generating time values
t = np.sort(np.random.uniform(0, 100, N))

# Model for ONE planet
vr = K1 * np.sin(2 * np.pi * t / P1 + phi1)
vr = K1 * np.sin(2 * np.pi * t / P1 + phi1)

# Adding Noise
noise = 2.2
vel =  vr + np.random.normal(0, noise, N)

# Errors
errvel = np.random.normal(2, 0.5, size=len(t))

# Adding Gaussian Noise
noise = 2.2
vel = vr + np.random.normal(0, noise, N)

# Saving to CSV
df = pd.DataFrame({"errvel": errvel, "t": t, "vel": vel})
df.to_csv("rv_data_3.csv", index=False)

print(K1, P1)
print("Done")
