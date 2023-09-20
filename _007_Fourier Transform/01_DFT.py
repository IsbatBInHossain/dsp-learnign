from matplotlib import pyplot as plt, style
from assets import mysignals as sig
import math


def dft(x):
    N = int(len(x))
    X_real = [0] * N
    X_img = [0] * N

    for k in range(N):
        for n in range(N):
            X_real[k] += x[n] * math.cos(2*math.pi * k*n/N)
            X_img[k] -= x[n] * math.sin(2*math.pi * k*n/N)

    return X_real, X_img


freq_real, freq_img = dft(sig.InputSignal_1kHz_15kHz)
style.use('ggplot')

f, axs = plt.subplots(3, sharex=True)

f.suptitle('DFT')

titles = ['Input Signal',
          'Frequency Domain (Real)', 'Freqency Domain (Imaginary)']
signals = [sig.InputSignal_1kHz_15kHz, freq_real, freq_img]

for ax, data, title in zip(axs, signals, titles):
    ax.plot(data)
    ax.set_title(title)

plt.show()
