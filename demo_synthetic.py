from tim import TemporalInductionMesh
import numpy as np
import matplotlib.pyplot as plt

# Пример с синтетическими событиями
tim = TemporalInductionMesh(alpha=1.0, tau=2.0)

# Добавим события
for t in range(10):
    vec = np.random.rand(3)
    tim.add_event(t, vec)

# Посчитаем влияние
influences = tim.compute_influence()

# Отобразим
plt.plot(influences, marker='o')
plt.title("Temporal Influence (Synthetic Events)")
plt.xlabel("Event Index")
plt.ylabel("Total Influence")
plt.grid(True)
plt.show()
