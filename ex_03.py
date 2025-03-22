"""f(x) = x^3 - x - 2"""

import matplotlib.pyplot as plt
import numpy as np

def resolve(x):
    return x**3 -x -2

def limite(maior, menor):

    mediana = maior - ((maior - menor) /2)
    print("a mediana é: " + str(mediana))
    
    y = resolve(mediana)
    print("o y é: " + str(y))
    if y > 0:
        return limite(mediana, menor)
    elif y < 0:
        return limite(maior, mediana)
    else:
        return mediana

        




while True:
    maior = float(input("digite o maior valor do intervalo: "))
    menor = float(input("digite o menor valor do intervalo: "))
    
    res = limite(maior, menor)
    print("dentro desse limite existe raiz no valor de x = " + str(res))

    print("\n\nesse intervalo não tem raízes")



