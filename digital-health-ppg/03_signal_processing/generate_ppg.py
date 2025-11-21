import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate synthetic PPG signal
fs = 100  # sampling frequency
t = np.linspace(0, 10, fs * 10)  # 10 seconds

# Basic PPG shape: pulsatile waveform using sine + added features
heart_rate = 75  # bpm
ppg = 0.6 * np.sin(2 * np.pi * (heart_rate/60) * t)  # base signal
ppg += 0.05 * np.random.randn(len(t))  # add noise

# Plot
plt.plot(t, ppg)
plt.title("Synthetic PPG Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Save data
df = pd.DataFrame({"time": t, "ppg": ppg})
df.to_csv("data/raw/ppg_day2.csv", index=False)

print("Synthetic PPG signal generated and saved!")
