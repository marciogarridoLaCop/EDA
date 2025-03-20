# Passos manuais para resolver o sistema de equações
passos = [
    "1. Igualamos as equações: 0.5x + 0.5 = -x + 2",
    "2. Somamos x em ambos os lados: 0.5x + x + 0.5 = 2",
    "3. Simplificamos: 1.5x + 0.5 = 2",
    "4. Subtraímos 0.5 em ambos os lados: 1.5x = 1.5",
    "5. Dividimos por 1.5: x = 1",
    "6. Substituímos x = 1 em y = 0.5x + 0.5",
    "7. Calculamos: y = 0.5(1) + 0.5 = 1",
    "8. A solução do sistema é (1,1)"
]

for passo in passos:
    print(passo)


# Resolvendo de maneira manual o sistema de equações (nao e a melhor forma, mas atende)
def resolver_sistema(eq1, eq2):
    print("\n🔹 PASSO 1: Definição do Sistema")
    print(f"   {eq1}")
    print(f"   {eq2}")

    print("\n🔹 PASSO 2: Igualamos as equações:")
    print("   0.5x + 0.5 = -x + 2")

    print("\n🔹 PASSO 3: Somamos x em ambos os lados:")
    x_coef = 0.5 + 1  
    print(f"   {x_coef}x + 0.5 = 2")

    print("\n🔹 PASSO 4: Subtraímos 0.5 em ambos os lados:")
    constante = 2 - 0.5  
    print(f"   {x_coef}x = {constante}")

    print("\n🔹 PASSO 5: Dividimos ambos os lados por 1.5:")
    x = constante / x_coef  
    print(f"   x = {x}")

    print("\n🔹 PASSO 6: Substituímos x = 1 em y = 0.5x + 0.5:")
    y = 0.5 * x + 0.5  
    print(f"   y = {y}")

    print("\n🔹 SOLUÇÃO FINAL:")
    print(f"   (x, y) = ({x}, {y})")



eq1_input = "y = 0.5x + 0.5"
eq2_input = "y = -x + 2"

resolver_sistema(eq1_input, eq2_input)
