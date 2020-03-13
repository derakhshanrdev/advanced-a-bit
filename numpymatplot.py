import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
sinx = np.sin(x)
plt.plot(x, sinx)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('sine wave')
plt.xlim([0, 4*np.pi])
plt.ylim([-1.5, 1.5])
plt.show()






