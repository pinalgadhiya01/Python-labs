import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000         
t = np.linspace(0, 1, fs, endpoint=False) 

# Frequencies of the sine waves
f1 = 5   
f2 = 10  

# Generate sine waves
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)

combined_signal = signal1 + signal2

# Plotting
plt.figure(figsize=(12, 8))

# First sine wave
plt.subplot(3, 1, 1)
plt.plot(t, signal1)
plt.title('Sine Wave 1 (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Second sine wave
plt.subplot(3, 1, 2)
plt.plot(t, signal2)
plt.title('Sine Wave 2 (10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Combined signal
plt.subplot(3, 1, 3)
plt.plot(t, combined_signal)
plt.title('Combined Signal (5 Hz + 10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
