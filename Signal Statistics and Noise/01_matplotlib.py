from matplotlib import pyplot as plt
from matplotlib import style

x = [1, 2, 3, 4, 5, 6]
y = [1, 6, 4, 4, 7, 2]
y2 = [3, 4, 7, 4, 2, 6]

style.use('dark_background')
plt.plot(x, y, label='line one')
plt.plot(x, y2, label='line two')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Chart 1')
plt.legend()
plt.show()
