
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tim_core import compute_influence_matrix, total_influence

# Synthetic anomaly time-series
np.random.seed(42)
times = np.arange(50)
cpu = np.sin(times / 5) + np.random.normal(0, 0.2, size=50)
cpu[30:33] += 3  # Inject anomaly

events = cpu.reshape(-1, 1)
inf_matrix = compute_influence_matrix(events, times, alpha=1.0, tau=5.0)
total_inf = total_influence(inf_matrix)

plt.figure(figsize=(10,4))
plt.plot(times, cpu, label="CPU Usage")
plt.plot(times, total_inf, label="TIM Influence", linestyle="--")
plt.axvspan(30, 32, color='red', alpha=0.2, label="True Anomaly")
plt.legend()
plt.title("TIM Influence vs Anomaly")
plt.xlabel("Time")
plt.ylabel("Signal / Influence")
plt.show()
