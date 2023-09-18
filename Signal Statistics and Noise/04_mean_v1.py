import numpy as np
from assets import mysignals as sig
from matplotlib import pyplot as plt

signal_mean = np.mean(sig.InputSignal_1kHz_15kHz)
print(signal_mean)
