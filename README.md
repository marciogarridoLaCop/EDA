# Universidade de Vassouras


![N|Solid](https://univassouras.edu.br/wp-content/uploads/2023/10/UniVassouras-Horizontal-Colorida.png)
# Conheca o Curso de Engenharia de Software 
[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/Simbolo_Engenharia_de_Software.jpg)](https://universidadedevassouras.edu.br/graduacao-marica/engenharia-de-software/)
## Estrutura-de-dados-avançados
# Exercício 01

Desenvolva um algoritmo que seja capaz de resolver um sistema de equações lineares abaixo 

$$
\begin{cases}
y = 0.5x + 0.5 \\
y = -x + 2
\end{cases}
$$

Como resultado, sua saída devera apresentar o resultado do sistema de equações e plotar as equações, o ponto x,y 

# Exercício 02

O problema que usaremos é bem conhecido e bastante simples. Queremos resolver uma equação de segundo grau, ou seja, dada a equação : 𝒂𝒙𝟐 + 𝒃𝒙 + 𝒄, queremos saber quais são as suas raízes reais, se elas existirem. Desta forma, resolva a função 2𝑥ˆ2 + 2𝑥 − 6.

# Exercícios 03
![N|Solid](https://github.com/marciogarridoLaCop/EDA/blob/main/grafico.jpg)


# **Encontrando um ponto dentro de uma Função**

Como engenheiro de software voce recebeu a missão de encontrar o valor aproximado de \( x \) que faz com que uma determinada função \( f(x) \) seja igual a zero.

Para isso, como explicado nas aulas anteriores você sabe que o valor deverá ser investigado dentro de um intervalo \([a, b]\), onde:

- \( f(a) \) e \( f(b) \) possuem sinais opostos (um é positivo e o outro é negativo).

O seu objetivo é criar um algoritmo que, a cada etapa, reduza esse intervalo até obter um valor de \( x \) com um erro aceitável.

## **Passos:**
1. Escolha um ponto médio \( m \) entre \( a \) e \( b \).
2. Avalie \( f(m) \).
3. Se \( f(m) \) for suficientemente próximo de zero, pare. Caso contrário:
   - Se \( f(m) \) e \( f(a) \) tiverem sinais opostos, então a raiz está entre \( a \) e \( m \), e você deve descartar \( b \).
   - Caso contrário, o valor de interesse está entre \( m \) e \( b \), e você deve descartar \( a \).
4. Repita o processo até atingir a precisão desejada.

Aplique esse método para encontrar este ponto na função:

\[
f(x) = x^3 - x - 2
\]

no intervalo \([1, 2]\) com uma precisão de \( 10^{-4} \).


# Exercícios 04
Um engenheiro de automação capturou durante um período de 30 dias [Dados Climáticos](https://github.com/marciogarridoLaCop/EDA/blob/main/dadosclimaticos.txt), diversos valores de temperatura, umidade e pressão de um ambiente específico. Sabendo que o acumulado de 24 horas foi a resultante de aporte de n ciclos de 10 minutos, calcule:

1) Para todas as grandezas climáticas, os valores mínimos, máximos, médios em 24 horas de um do vigésimo dia;
2) A quantidade de ciclos por período de coleta neste dia.

# Exercícios 05
Enunciado: Árvore Genealógica

Imagine que você recebeu a tarefa de criar uma árvore genealógica para uma família. A árvore deve ser capaz de armazenar informações sobre várias gerações de uma família e suas relações.

Requisitos:

Modelo de Dados:

Cada membro da família deve ser representado como um dicionário contendo: nome, idade, sexo e uma lista de filhos.
A lista de filhos de cada membro da família deve conter dicionários representando cada filho.
Funções a serem implementadas:

adicionar_membro(nome, idade, sexo, pai=None): Adiciona um membro à árvore genealógica. Se o pai for especificado, o membro é adicionado como filho desse pai.
buscar_membro(nome): Retorna o dicionário representando o membro da família com o nome especificado.
descendentes(nome): Retorna uma lista de todos os descendentes do membro com o nome especificado. Esta função deve ser implementada de forma recursiva.
Exemplo de Uso:

Adicione um membro chamado "João" com 70 anos.
Adicione um filho para "João" chamado "Carlos" com 50 anos.
Adicione um filho para "Carlos" chamado "Pedro" com 30 anos.
Adicione um filho para "Pedro" chamado "Lucas" com 10 anos.
Ao chamar a função descendentes("João"), ela deve retornar uma lista contendo "Carlos", "Pedro" e "Lucas".
Desafio Extra:

Implemente uma função antepassados(nome) que, dado o nome de um membro, retorna uma lista de todos os seus antepassados diretos (pai, avô, bisavô, etc.). Esta função também deve ser implementada de forma recursiva.
Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.
