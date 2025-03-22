import numpy as np
import matplotlib.pyplot as plt


def eq1(x):
    return 0.5*x + 0.5


def eq2(x):
    return -x + 2


x = np.linspace(-2, 3, 400)


y1 = eq1(x)
y2 = eq2(x)

plt.plot(x, y1, label=r'$y = 0.5x + 0.5$', color='blue')
plt.plot(x, y2, label=r'$y = -x + 2$', color='red')

plt.scatter(1, 1, color='green', zorder=5)
plt.text(1, 1, '(1, 1)', fontsize=12, verticalalignment='bottom')

plt.xlim(-2, 3)
plt.ylim(-2, 3)


plt.title("Solução do sistema de equações lineares")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)

plt.legend()

plt.show()