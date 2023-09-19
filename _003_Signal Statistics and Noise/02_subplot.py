from matplotlib import pyplot as plt
from matplotlib import style

from assets import mysignals as sig

inputSignal = sig.InputSignal_1kHz_15kHz

style.use('ggplot')
style.use('dark_background')

f, plt_arr = plt.subplots(3, sharex=True)
colors = ['Red', 'Green', 'Blue']
f.suptitle('Multiplot')
for i in range(len(plt_arr)):
    plt_arr[i].plot(inputSignal, color=colors[i])
    plt_arr[i].set_title(f'Subtitle {i+1}', color=colors[i])

plt.show()
