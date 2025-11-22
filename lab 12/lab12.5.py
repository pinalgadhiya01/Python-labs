import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500       
T = 2            
t = np.arange(0, T, 1/fs)

# Original sine wave
x = np.sin(2 * np.pi * 5 * t)

# Time-reversed signal
x_reversed = x[::-1]        
t_reversed = t[::-1]          

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, x, label='Original 5 Hz Sine')
plt.plot(t_reversed, x_reversed, label='Time-Reversed', linestyle='--')
plt.title("Original vs. Time-Reversed 5 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
