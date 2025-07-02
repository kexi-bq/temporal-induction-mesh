
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_influence_matrix(events, times, alpha=1.0, tau=1.0):
    n = len(events)
    influence_matrix = np.zeros((n, n))
    sim_matrix = cosine_similarity(events)
    for i in range(n):
        for j in range(i+1, n):
            dt = times[j] - times[i]
            if dt > 0:
                decay = np.exp(-dt / tau)
                influence_matrix[i, j] = alpha * decay * sim_matrix[i, j]
    return influence_matrix

def total_influence(influence_matrix):
    return np.sum(influence_matrix, axis=0)
