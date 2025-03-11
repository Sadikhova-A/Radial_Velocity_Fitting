import numpy as np
import pandas as pd

# Parameters
P1 = 25
K1 = np.random.normal(9, 4)
phi1 = np.random.uniform(0, 2*np.pi)

# Generating time values
t = np.sort(np.random.uniform(0, 100, 50))

# Model for ONE planet
vel = K1 * np.sin(2 * np.pi * t / P1 + phi1)

# Errors
errvel = np.random.normal(2, 0.5, size=len(t))

# Saving to CSV
df = pd.DataFrame({"errvel": errvel, "t": t, "vel": vel})
df.to_csv("rv_data_1.csv", index=False)

print(K1)
print("Done")
