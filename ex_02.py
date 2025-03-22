
"""
    2𝑥ˆ2 + 2𝑥 − 6
    -b +- sqrt(b²-4ac) / 2a"""

import matplotlib.pyplot as plt
import numpy as np


def resolve():
    x1 = (-2 + (2**2 - 4*2*-6)**0.5) / 2*2
    x2 = (-2 + (2**2 + 4*2*-6)**0.5) / 2*2
    return x1,x2

delta = 2**2 - 4*2*-6

if delta >= 0:
    print(delta)
    x1, x2 = resolve()
    x2 = np.real(x2)
    print(f"os valores das raízes são {x1:.2f} e {x2:.2f}")