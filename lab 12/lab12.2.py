import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500         
T = 2             
t = np.arange(0, T, 1/fs)  

# Signals
sine_5Hz = np.sin(2 * np.pi * 5 * t)
cos_10Hz = np.cos(2 * np.pi * 10 * t)

product_signal = sine_5Hz * cos_10Hz

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, product_signal)
plt.title("Product of 5 Hz Sine Wave and 10 Hz Cosine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
