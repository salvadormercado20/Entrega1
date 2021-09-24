import numpy as np


a = np.arange(78000)
b = np.random.choice(a, 60000)

def metricas(z):
    return np.mean(z),np.median(z),np.var(z)


