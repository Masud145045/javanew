
# Linear Antenna Array (2D)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 8
d = 0.5
k = 2 * np.pi
beta = 0

# Angle values
theta = np.linspace(0, 2*np.pi, 1000)

# Array Factor
AF = np.zeros_like(theta, dtype=complex)

for n in range(N):
    AF += np.exp(1j * n * (k * d * np.cos(theta) + beta))

AF = np.abs(AF)
AF = AF / np.max(AF)

# Plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, AF)
ax.set_ylim(0, 1)
ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_title("Linear Antenna Array (2D)")

plt.show()