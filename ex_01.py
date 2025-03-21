"""{
y=0.5x+0.5
y=-x+2}"""

import matplotlib.pyplot as plt
import numpy as np

def resolve(x):
    y1 = 0.5 * x + 0.5
    y2 = x * -1 + 2
    
    return y1,y2
    
def cria_vetores(max_X):
    vals_x = []
    vals_y1 = []
    vals_y2 = []
    for i in range(max_X):
        vals_y1.append(resolve(i))
        vals_y2.append(resolve(i))
        vals_x.append(i)
    return vals_x, vals_y1, vals_y2
    
def des_linha(vals_x, vals_y1, vals_y2):
    plt.plot(vals_x, vals_y1)
    plt.plot(vals_x, vals_y2)
    plt.show()
    
while True:
    max_X = int(input("diga o valor maximo de X: "))
    vals_x, vals_y1, vals_y2 = cria_vetores(max_X)      
    des_linha(vals_x, vals_y1, vals_y2)