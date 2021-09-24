
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

a = np.arange(78000)
b = np.random.choice(a, 60000)
def filters(z):
        x=z.T
        high_cutoff_bp = 1 / (10000 / 2)
        low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, [high_cutoff_bp, low_cutoff_bp], btype='bandpass')
        b1, a1 = signal.butter(2, low_cutoff_bp, btype='lowpass')
        b2, a2 = signal.butter(2, high_cutoff_bp, btype='highpass')
        plt.plot(x)
        return signal.filtfilt(b, a, x.T), signal.filtfilt(b1, a1, x.T), signal.filtfilt(b2, a2, x.T)
        

filters(b)

