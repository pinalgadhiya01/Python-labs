import numpy as np

zeros = np.array([0.7, 0.9])
poles = np.array([0.6, 0.4])

print("Zeros:", zeros)
print("Poles:", poles)

# Check stability
stable = np.all(np.abs(poles) < 1)

if stable:
    print("\nThe system is STABLE.")
else:
    print("\nThe system is UNSTABLE.")
