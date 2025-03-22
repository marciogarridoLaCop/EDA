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



