from matplotlib import pyplot as plt, style
from assets import mysignals as sig
import math


def dft(x):
    N = int(len(x)/2)
    X_real = [0] * N
    X_img = [0] * N
    X_mag = [0.0] * N

    for k in range(N):
        for n in range(len(x)):
            X_real[k] += x[n] * math.cos(2*math.pi * k*n/len(x))
            X_img[k] -= x[n] * math.sin(2*math.pi * k*n/len(x))
            X_mag[k] = math.sqrt(X_real[k]**2 + X_img[k]**2)

    return X_real, X_img, X_mag


freq_real, freq_img, freq_mag = dft(sig.InputSignal_1kHz_15kHz)
style.use('ggplot')

f, axs = plt.subplots(4, sharex=True)

f.suptitle('DFT')

titles = ['Input Signal',
          'Frequency Domain (Real)', 'Freqency Domain (Imaginary)', 'Frequency Domain (Mag)']
signals = [sig.InputSignal_1kHz_15kHz, freq_real, freq_img, freq_mag]

for ax, data, title in zip(axs, signals, titles):
    ax.plot(data)
    ax.set_title(title)

plt.show()
