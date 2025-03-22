"""{
y=0.5x+0.5
y=-x+2}"""

import matplotlib.pyplot as plt


def resolve(x):
    y1 = 0.5 * x + 0.5
    y2 = x * -1 + 2
    y3 = (1.5*x +2.5)/2
    return y1,y2,y3
    
def cria_vetores(max_X):
    vals_x = []
    vals_y1 = []
    vals_y2 = []
    vals_y3 = []
    for i in range(max_X):
        y1, y2, y3 = resolve(i)
        vals_y1.append(y1)
        vals_y2.append(y2)
        vals_y3.append(y3)
        vals_x.append(i)
        if y1 == y2:
            plt.scatter(i,y1, color="black", label="interseção")
    return vals_x, vals_y1, vals_y2, vals_y3
    
def des_linha(vals_x, vals_y1, vals_y2, vals_y3):
    plt.plot(vals_x, vals_y1, color='blue', label='equação 1')
    plt.plot(vals_x, vals_y2, color='red', label='equação 2')
    plt.plot(vals_x, vals_y3, color='green', label='soma')
    plt.legend()
    plt.show()
    
while True:
    max_X = int(input("diga o valor maximo de X: "))
    vals_x, vals_y1, vals_y2, vals_y3 = cria_vetores(max_X)      
    des_linha(vals_x, vals_y1, vals_y2, vals_y3)
    print("o resultado do sistema de equações é: y=(1.5*x + 2.5)/2")