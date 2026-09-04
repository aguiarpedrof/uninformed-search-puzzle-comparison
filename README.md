# Análise Comparativa de Métodos de Busca Não Informada no Jogo das Peças

Implementação, análise de desempenho e estudo comparativo entre os métodos de busca cega **Busca em Largura (BFS)**, **Busca em Profundidade (DFS)** e **Backtracking Recursivo** aplicados ao problema clássico do Jogo das Peças Brancas e Pretas. O projeto reproduz e valida em Python as especificações formais originalmente desenvolvidas em Prolog (`prog21.pl` e `prog22.pl`).

---

## 1. Definição Formal do Espaço de Estados

O problema consiste em um tabuleiro unidimensional composto por 5 posições, contendo duas peças brancas (`B`), duas peças pretas (`P`) e um espaço vazio (`_`).

* **Representação:** Lista de inteiros onde `1 = B`, `2 = P` e `0 = _`.
* **Estado Inicial ($E_0$):** `[1, 1, 0, 2, 2]` $\rightarrow$ `[B, B, _, P, P]`
* **Estado Meta ($E_{\text{meta}}$):** `[1, 2, 2, 1, 0]` $\rightarrow$ `[B, P, P, B, _]`

### Operadores de Transição
1. **Deslisa (Distância 1):** Troca o espaço vazio com a peça adjacente imediata à esquerda ou à direita.
2. **Salta (Distância 2):** Troca o espaço vazio saltando uma peça intermediária (à esquerda ou à direita).

---

## 2. Métodos de Busca Implementados

1. **Busca em Largura (BFS - Breadth-First Search):**
   * Estrutura: Fila FIFO (`collections.deque`).
   * Exploração por níveis com detecção de ciclo por ramo.
   * Garante a solução de menor número de passos (otimalidade de comprimento).

2. **Busca em Profundidade (DFS - Depth-First Search):**
   * Estrutura: Pilha LIFO explícita.
   * Expansão em lote (equivalente ao predicado `findall` do Prolog).
   * Segue até a profundidade máxima permitida pela ausência de ciclos.

3. **Backtracking Recursivo:**
   * Estrutura: Pilha de execução da recursão.
   * Explora um único operador por vez; havendo falha ou ciclo, retrocede ao ponto de escolha anterior.

---

## 3. Estrutura do Repositório

```text
├── solucao_busca.py    # Implementação dos algoritmos BFS, DFS e Backtracking
├── Slides/
│   ├── if-beamer.cls   # Classe LaTeX Beamer (UNIFEI)
│   ├── main.tex        # Apresentação técnica em LaTeX Beamer
│   ├── main.pdf        # Documento PDF compilado
│   └── figuras/        # Recursos gráficos da apresentação
└── README.md           # Documentação técnica do projeto
```

---

## 4. Requisitos e Instruções de Execução

### Requisitos
* Python 3.8 ou superior (sem dependências externas).

### Execução
Para executar os três algoritmos e visualizar a trajetória completa com o quadro comparativo:
```bash
python solucao_busca.py
```

---

## 5. Quadro Comparativo de Resultados

Resultados experimentais obtidos para a transição $E_0 \rightarrow E_{\text{meta}}$:

| Método de Busca | Passos na Solução | Nós Visitados | Tempo Médio (ms) | Solução Ótima? | Complexidade de Tempo | Complexidade Espacial |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Busca em Largura (BFS)** | **4** | 20 | ~0.038 | **Sim** | $\mathcal{O}(b^d)$ | $\mathcal{O}(b^d)$ (Fila) |
| **Busca em Profundidade (DFS)** | 16 | 20 | ~0.037 | Não | $\mathcal{O}(b^m)$ | $\mathcal{O}(b \cdot m)$ (Pilha) |
| **Backtracking Recursivo** | 16 | 20 | ~0.166 | Não | $\mathcal{O}(b^m)$ | $\mathcal{O}(m)$ (Recursão) |

*Onde $b$ é o fator de ramificação médio, $d$ é a profundidade da solução ótima e $m$ é a profundidade máxima da árvore.*

### Trajetória da Solução Ótima (BFS - 4 passos):
1. `[B, B, _, P, P]` $\xrightarrow{\text{salta}}$ `[B, B, P, P, _]`
2. `[B, B, P, P, _]` $\xrightarrow{\text{deslisa}}$ `[B, B, P, _, P]`
3. `[B, B, P, _, P]` $\xrightarrow{\text{salta}}$ `[B, _, P, B, P]`
4. `[B, _, P, B, P]` $\xrightarrow{\text{salta}}$ `[B, P, P, B, _]` (Meta alcançada)

---

## 6. Autores

* **Iago Vieira Vilela**
* **Pedro Fernandes Aguiar**

Instituição: Universidade Federal de Itajubá (UNIFEI)  
Disciplina: ECOI2217 - Inteligência Artificial

---

## 7. Referências Bibliográficas

* RUSSELL, Stuart; NORVIG, Peter. **Artificial Intelligence: A Modern Approach**. 4. ed. Pearson, 2021.
* UNIFEI. **ECOI2217 - Inteligência Artificial**: Programas em Prolog `prog21.pl` e `prog22.pl`, 2026.
