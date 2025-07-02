import numpy as np
from scipy.spatial.distance import cosine
import math

class Event:
    def __init__(self, time, features):
        self.time = time
        self.features = np.array(features)

class TemporalInductionMesh:
    def __init__(self, alpha=1.0, tau=1.0):
        self.alpha = alpha
        self.tau = tau
        self.events = []

    def add_event(self, time, features):
        self.events.append(Event(time, features))

    def similarity(self, x, y):
        return 1 - cosine(x, y)

    def compute_influence(self):
        influences = []
        for j, ej in enumerate(self.events):
            rho = 0
            for i, ei in enumerate(self.events[:j]):
                delta_t = abs(ej.time - ei.time)
                decay = math.exp(-delta_t / self.tau)
                sim = self.similarity(ei.features, ej.features)
                r_ij = self.alpha * decay * sim
                rho += r_ij
            influences.append(rho)
        return influences
