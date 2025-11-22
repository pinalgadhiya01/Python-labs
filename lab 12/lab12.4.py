import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500        
T = 1             
t = np.arange(0, T, 1/fs)

x = np.sin(2 * np.pi * 10 * t)

# Scaled signal (amplitude × 3)
x_scaled = 3 * x

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, x, label='Original 10 Hz Sine')
plt.plot(t, x_scaled, label='Scaled (×3 Amplitude)', linestyle='--')
plt.title("Original vs. Scaled 10 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
