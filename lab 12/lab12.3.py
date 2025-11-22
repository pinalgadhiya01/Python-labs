import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500       
T = 2             
t = np.arange(0, T, 1/fs)  

# Original signal
x = np.sin(2 * np.pi * 5 * t)

# Time shift of +0.1 s (delay)
shift = 0.1
t_shifted = t + shift
x_shifted = np.sin(2 * np.pi * 5 * t_shifted)

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, x, label='Original 5 Hz Sine')
plt.plot(t, x_shifted, label='Shifted by 0.1 s', linestyle='--')
plt.title("5 Hz Sine Wave: Original vs. Time-Shifted")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
