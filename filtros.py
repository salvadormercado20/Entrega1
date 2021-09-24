
import scipy.io as sio
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
import pywt
from scipy import signal

path = './'

mat_contents = sio.loadmat(path + 'P001_S0_P1', squeeze_me = True)

def bandPass(mat_contents):
    for i in range(1,5):
        ACC = mat_contents['Data'][i]
        x=ACC.T
        high_cutoff_bp = 1 / (10000 / 2)
        low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, [high_cutoff_bp, low_cutoff_bp], btype='bandpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)

def lowPass(mat_contents):
    for i in range(1,5):
        ACC = mat_contents['Data'][i]
        x=ACC.T
        #high_cutoff_bp = 1 / (10000 / 2)
        low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, low_cutoff_bp, btype='lowpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)
        
def highPass(mat_contents):
    for i in range(1,5):
        ACC = mat_contents['Data'][i]
        x=ACC.T
        high_cutoff_bp = 1 / (10000 / 2)
        #low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, high_cutoff_bp, btype='highpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)