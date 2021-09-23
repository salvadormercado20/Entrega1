import scipy.io as sio
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
import pywt
from scipy import signal

path = 'C:/Users/Lenovo/OneDrive - Instituto Tecnológico Metropolitano/Maestria/Tesis/Señales Tesis/Signals/Patients/P001/'

mat_contents = sio.loadmat(path + 'P001_S0_P2_A5.mat', squeeze_me = True)

def bandPass(mat_contents):
    for i in range(0,4):
        ACC = mat_contents['Data_ACC'][i]
        x=ACC.T
        high_cutoff_bp = 1 / (10000 / 2)
        low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, [high_cutoff_bp, low_cutoff_bp], btype='bandpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)

def lowPass(mat_contents):
    for i in range(0,4):
        ACC = mat_contents['Data_ACC'][i]
        x=ACC.T
        #high_cutoff_bp = 1 / (10000 / 2)
        low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, low_cutoff_bp, btype='lowpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)
        
def highPass(mat_contents):
    for i in range(0,4):
        ACC = mat_contents['Data_ACC'][i]
        x=ACC.T
        high_cutoff_bp = 1 / (10000 / 2)
        #low_cutoff_bp = 300 / (10000 / 2)
        b, a = signal.butter(2, high_cutoff_bp, btype='highpass')
        x_filt = signal.filtfilt(b, a, x.T)
        plt.figure()
        plt.plot(x_filt)
        plt.plot(ACC)

bandPass(mat_contents)
lowPass(mat_contents)
highPass(mat_contents)