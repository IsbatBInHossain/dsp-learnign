from assets import mysignals as sig
from matplotlib import style as stl, pyplot as plt

stl.use('ggplot')

f, plt_arr = plt.subplots(2, sharex=True)

f.suptitle('Input signal and Impulse response')

plt_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plt_arr[1].plot(sig.Impulse_response)

plt.show()
