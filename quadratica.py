import numpy as np
import matplotlib.pyplot as plt

def extrair_coeficientes(equacao):
   
    equacao = equacao.replace(" ", "")
    a, b, c = 0.0, 0.0, 0.0  

  
    termos = equacao.replace("-", "+-").split("+")  
    for termo in termos:
        if "x^2" in termo: 
            coef = termo.replace("x^2", "")
            a = float(coef) if coef not in ["", "+", "-"] else float(coef + "1")  
        elif "x" in termo:  
            coef = termo.replace("x", "")
            b = float(coef) if coef not in ["", "+", "-"] else float(coef + "1")
        elif termo:  
            c = float(termo)
    
    return a, b, c

def f(x, a, b, c):
   
    return a*x**2 + b*x + c

def calcular_raizes(a, b, c):
  
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None  
    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)
    return x1, x2



equacao = input("Digite a equação no formato ax^2 + bx + c: ")
a, b, c = extrair_coeficientes(equacao)

print(f"Coeficientes extraídos: a={a}, b={b}, c={c}")

x1, x2 = calcular_raizes(a, b, c)


if x1 is not None and x2 is not None:
    x_lim = max(abs(x1), abs(x2)) + 2
else:
    x_lim = 10  
x_min, x_max = -x_lim, x_lim

# Criar pontos para o gráfico
x = np.linspace(x_min, x_max, 400)
y = f(x, a, b, c)

# Plotar a função
plt.figure(figsize=(8,6))
plt.plot(x, y, label=f"y = {equacao}", color="blue")


if x1 is not None and x2 is not None:
    plt.scatter([x1, x2], [0, 0], color="red", zorder=3)  
    plt.text(x1, 2, f'x1 = {x1:.3f}', horizontalalignment='center', color="red")
    plt.text(x2, -2, f'x2 = {x2:.3f}', horizontalalignment='center', color="red")


plt.ylim(-10, 25)
plt.title(f"Gráfico de y = {equacao}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=2.5)
plt.axvline(0, color='black', linewidth=2.5)
plt.legend()
plt.show()
