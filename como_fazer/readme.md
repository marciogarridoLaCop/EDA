# 📘 Guia de Colaboração – Resolução de Exercícios de Estrutura de dados Avançados (2 pontos)

Este arquivo mostra passo a passo como você deve trabalhar com este repositório para resolver os exercícios da disciplina de **Estrutura de Dados Avancados - Atividade P1**, de forma organizada e rastreável.

Seu progresso será acompanhado individualmente com base em **commits, branches e pull requests**. 

---

## 🔗 Repositório de Base

Repositório original com os exercícios:  
➡️ **https://github.com/marciogarridoLaCop/EDA**

---

## 🔄 Fase 1 – Fork do Repositório

1. Acesse o repositório acima.
2. Clique em **Fork** (no canto superior direito).
3. Um repositório igual será criado na sua conta do GitHub.

---

## 💻 Fase 2 – Clone do seu Fork

1. Acesse seu repositório forkado no GitHub.
2. Clique em **Code > HTTPS** e copie o link.
3. No terminal/git bash, rode:

```bash
git clone https://github.com/SEU_USUARIO/EDA.git
cd EDA
```

> Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

---

## 🌿 Fase 3 – Criação de Branch por Exercício

Antes de começar cada exercício, crie uma nova branch com o seguinte padrão:

```bash
git checkout -b exercicio-01
```

> Use `exercicio-02`, `exercicio-03` e assim por diante para os próximos.

---

## ✍️ Fase 4 – Desenvolvimento com Commits Frequentes

Durante a resolução:

1. Crie ou edite o arquivo `.py` correspondente ao exercício.
2. Faça commits frequentes para mostrar sua evolução.

```bash
git add .
git commit -m "Inicia exercício 01 com estrutura base"
git commit -m "Adiciona lógica de ordenação"
git commit -m "Corrige erro no laço de repetição"
```

> **Dica:** Commits pequenos e explicativos são bem-vindos!

---

## ⬆️ Fase 5 – Push da Branch para o GitHub

Quando tiver feito progresso (ou finalizado), envie a branch para seu repositório remoto:

```bash
git push origin exercicio-01
```

---

## 🔀 Fase 6 – Criar um Pull Request para o repositório original

1. Vá até o **seu repositório** no GitHub.
2. Clique em **"Compare & Pull Request"**.
3. Verifique se a base do PR é a `main` do repositório original.
4. Preencha assim:

- **Título:** `[Seu Nome] - Exercício 01`
- **Descrição:** Comente o que foi feito, se teve dificuldades, melhorias futuras etc.

Depois clique em **Create Pull Request**.

---

## 🔁 Fase 7 – Repetição do processo

Para os próximos exercícios:

```bash
git checkout main
git pull origin main
git checkout -b exercicio-02
```

Depois, repita todo o ciclo: desenvolva, faça commits, push e PR.

---

## 📊 Fase 8 – Avaliação da Entrega

As entregas serão avaliadas com base em:
- ✅ Os exercícios atendendo ao enunciado (0.5 pontos)
- ✅ **Commits** frequentes e bem descritos (0.25 pontos)
- ✅ Uso correto de **branches separadas** (0.25 pontos)
- ✅ Organização e lógica do **código** (0.50 pontos)
- ✅ Clareza na descrição dos **pull requests** (0.25 pontos)
- ✅ Participação ativa e evolução visível (0.25 pontos)



