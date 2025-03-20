def obter_coeficientes(equacao):
    """Extrai os coeficientes a, b e c da equação no formato ax + by = c"""
    equacao = equacao.replace(" ", "")  # Remover espaços que por ventura o usuario digitou
    lados = equacao.split("=")

    if len(lados) != 2:
        print("Erro: A equação deve estar no formato ax + by = c")
        return None

    expressao_esquerda = lados[0]
    c = float(lados[1])  

    a = 0
    b = 0

    termos = expressao_esquerda.replace("-", "+-").split("+")  

    for termo in termos:
        if "x" in termo:
            coef = termo.replace("x", "")
            a = float(coef) if coef not in ["", "-"] else (1 if coef == "" else -1)
        elif "y" in termo:
            coef = termo.replace("y", "")
            b = float(coef) if coef not in ["", "-"] else (1 if coef == "" else -1)

    return a, b, c


def resolver_sistema(a1, b1, c1, a2, b2, c2):
   
    print("\n🔹 PASSO 1: Definição do Sistema")
    print(f"   {a1}x + {b1}y = {c1}")
    print(f"   {a2}x + {b2}y = {c2}")

    print("\n🔹 PASSO 2: Multiplicamos a primeira equação por", b2, "e a segunda por", b1, "para eliminar x")
    eq1_nova = (a1 * b2, b1 * b2, c1 * b2)
    eq2_nova = (a2 * b1, b2 * b1, c2 * b1)

    print(f"   {eq1_nova[0]}x + {eq1_nova[1]}y = {eq1_nova[2]}")
    print(f"   {eq2_nova[0]}x + {eq2_nova[1]}y = {eq2_nova[2]}")


    novo_b = eq1_nova[1] - eq2_nova[1]
    novo_c = eq1_nova[2] - eq2_nova[2]
    y = novo_c / novo_b  

    print("\n🔹 PASSO 3: Eliminamos x e resolvemos para y")
    print(f"   {novo_b}y = {novo_c}")
    print(f"   y = {y}")

  
    print("\n🔹 PASSO 4: Substituímos y na equação original para encontrar x")
    x = (c1 - b1 * y) / a1
    print(f"   x = ({c1} - {b1}*{y}) / {a1}")
    print(f"   x = {x}")

    print("\n🔹 SOLUÇÃO FINAL:")
    print(f"   (x, y) = ({x}, {y})")


# Entrada do capiroto
print("Digite as equações no formato 'ax + by = c':")
eq1 = input("Equação 1: ")
eq2 = input("Equação 2: ")

# Obter coeficientes das equações
coef1 = obter_coeficientes(eq1)
coef2 = obter_coeficientes(eq2)

if coef1 and coef2:
    resolver_sistema(*coef1, *coef2)
