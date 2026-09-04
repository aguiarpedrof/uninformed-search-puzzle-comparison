"""
===============================================================================
ECOI2217 - Inteligência Artificial
Atividade 02 - Comparação dos Métodos de Busca (BFS, DFS e Backtracking)

Problema: Jogo das Peças Brancas e Pretas

Autor 1: Iago Vieira Vilela
Auror 2: Pedro Fernandes Aguiar
Data: 2026

Descrição:
Este script implementa e compara três estratégias de busca no espaço de estados:
1. Busca em Largura (BFS)
2. Busca em Profundidade (DFS)
3. Busca por Backtracking (Recursivo)
===============================================================================
"""

import time
from collections import deque

# Definição dos estados constante
ESTADO_INICIAL = [1, 1, 0, 2, 2]
ESTADO_META = [1, 2, 2, 1, 0]

# Mapeamento para exibição amigável dos estados
SIMBOLOS = {1: 'B', 2: 'P', 0: '_'}


def formatar_estado(estado):
    """Retorna o estado formatado como uma string (ex: [B, B, _, P, P])."""
    return "[" + ", ".join(SIMBOLOS[x] for x in estado) + "]"


def obter_transicoes(estado):
    """
    Gera as transições válidas a partir de um estado fornecido.
    Mapeia exatamente as regras 'transforma' do Prolog original.
    
    Retorna uma lista de tuplas: (nome_operacao, novo_estado)
    """
    idx_zero = estado.index(0)
    transicoes = []
    
    # Caso o espaço vazio esteja no índice 0
    if idx_zero == 0:
        # deslisa: traz elemento da pos 1
        novo = estado.copy()
        novo[0], novo[1] = novo[1], novo[0]
        transicoes.append(("deslisa", novo))
        
        # salta: traz elemento da pos 2
        novo = estado.copy()
        novo[0], novo[2] = novo[2], novo[0]
        transicoes.append(("salta  ", novo))

    # Caso o espaço vazio esteja no índice 1
    elif idx_zero == 1:
        # deslisa: traz elemento da pos 2
        novo = estado.copy()
        novo[1], novo[2] = novo[2], novo[1]
        transicoes.append(("deslisa", novo))
        
        # deslisa: traz elemento da pos 0
        novo = estado.copy()
        novo[1], novo[0] = novo[0], novo[1]
        transicoes.append(("deslisa", novo))
        
        # salta: traz elemento da pos 3
        novo = estado.copy()
        novo[1], novo[3] = novo[3], novo[1]
        transicoes.append(("salta  ", novo))

    # Caso o espaço vazio esteja no índice 2
    elif idx_zero == 2:
        # deslisa: traz elemento da pos 1
        novo = estado.copy()
        novo[2], novo[1] = novo[1], novo[2]
        transicoes.append(("deslisa", novo))
        
        # deslisa: traz elemento da pos 3
        novo = estado.copy()
        novo[2], novo[3] = novo[3], novo[2]
        transicoes.append(("deslisa", novo))
        
        # salta: traz elemento da pos 0
        novo = estado.copy()
        novo[2], novo[0] = novo[0], novo[2]
        transicoes.append(("salta  ", novo))
        
        # salta: traz elemento da pos 4
        novo = estado.copy()
        novo[2], novo[4] = novo[4], novo[2]
        transicoes.append(("salta  ", novo))

    # Caso o espaço vazio esteja no índice 3
    elif idx_zero == 3:
        # deslisa: traz elemento da pos 2
        novo = estado.copy()
        novo[3], novo[2] = novo[2], novo[3]
        transicoes.append(("deslisa", novo))
        
        # salta: traz elemento da pos 1
        novo = estado.copy()
        novo[3], novo[1] = novo[1], novo[3]
        transicoes.append(("salta  ", novo))
        
        # deslisa: traz elemento da pos 4
        novo = estado.copy()
        novo[3], novo[4] = novo[4], novo[3]
        transicoes.append(("deslisa", novo))

    # Caso o espaço vazio esteja no índice 4
    elif idx_zero == 4:
        # deslisa: traz elemento da pos 3
        novo = estado.copy()
        novo[4], novo[3] = novo[3], novo[4]
        transicoes.append(("deslisa", novo))
        
        # salta: traz elemento da pos 2
        novo = estado.copy()
        novo[4], novo[2] = novo[2], novo[4]
        transicoes.append(("salta  ", novo))

    return transicoes


# =============================================================================
# 1. BUSCA EM LARGURA (BFS - Breadth-First Search)
# =============================================================================
def busca_largura_bfs(estado_inicial, estado_meta):
    """
    Realiza a Busca em Largura (BFS) utilizando uma Fila (FIFO).
    Explora o espaço por níveis, garantindo encontrar a solução de menor caminho.
    
    Cada elemento da fila armazena o caminho percorrido até o estado atual:
    caminho = [(operacao, estado), ...]
    """
    inicio_tempo = time.perf_counter()
    
    # Fila de trajetórias (equivalente ao 'busca([[r(raiz, E)]], S)' do Prolog)
    caminho_inicial = [("raiz", estado_inicial)]
    fila = deque([caminho_inicial])
    
    nos_visitados = 0
    
    while fila:
        caminho_atual = fila.popleft()
        nos_visitados += 1
        
        _, ultimo_estado = caminho_atual[-1]
        
        # Verifica se atingiu a meta (atingemeta)
        if ultimo_estado == estado_meta:
            fim_tempo = time.perf_counter()
            return {
                "caminho": caminho_atual,
                "passos": len(caminho_atual) - 1,
                "nos_visitados": nos_visitados,
                "tempo_ms": (fim_tempo - inicio_tempo) * 1000
            }
        
        # Estende a trajetória gerando extensões válidas (estende e naoproduzcirculo)
        estados_no_caminho = [est for _, est in caminho_atual]
        
        for operacao, novo_estado in obter_transicoes(ultimo_estado):
            # Prevenção de ciclos: não produz círculo na mesma trajetória
            if novo_estado not in estados_no_caminho:
                novo_caminho = caminho_atual + [(operacao, novo_estado)]
                fila.append(novo_caminho)

    fim_tempo = time.perf_counter()
    return None


# =============================================================================
# 2. BUSCA EM PROFUNDIDADE (DFS - Depth-First Search)
# =============================================================================
def busca_profundidade_dfs(estado_inicial, estado_meta):
    """
    Realiza a Busca em Profundidade (DFS) utilizando uma Pilha (LIFO).
    Expande em lote (equivalente ao findall e ap(EXT, P, P1) do prog22.pl).
    
    Cada elemento da pilha armazena o caminho percorrido até o estado atual.
    """
    inicio_tempo = time.perf_counter()
    
    caminho_inicial = [("raiz", estado_inicial)]
    pilha = [caminho_inicial]
    
    nos_visitados = 0
    
    while pilha:
        caminho_atual = pilha.pop()
        nos_visitados += 1
        
        _, ultimo_estado = caminho_atual[-1]
        
        # Verifica se atingiu a meta
        if ultimo_estado == estado_meta:
            fim_tempo = time.perf_counter()
            return {
                "caminho": caminho_atual,
                "passos": len(caminho_atual) - 1,
                "nos_visitados": nos_visitados,
                "tempo_ms": (fim_tempo - inicio_tempo) * 1000
            }
        
        estados_no_caminho = [est for _, est in caminho_atual]
        
        # Gera extensões do estado atual (findall)
        extensoes = []
        for operacao, novo_estado in obter_transicoes(ultimo_estado):
            if novo_estado not in estados_no_caminho:
                extensoes.append(caminho_atual + [(operacao, novo_estado)])
        
        # Em prog22.pl: ap(EXT, P, P1) coloca EXT na frente de P.
        # Ao empilhar na ordem reversa, a primeira extensão de EXT fica no topo da pilha.
        for ext in reversed(extensoes):
            pilha.append(ext)

    fim_tempo = time.perf_counter()
    return None


# =============================================================================
# 3. BUSCA POR BACKTRACKING (RECURSIVO)
# =============================================================================
def busca_backtracking(estado_inicial, estado_meta):
    """
    Realiza a Busca por Backtracking Recursivo puro.
    Ao contrário do DFS em lote, testa um operador por vez na pilha de recursão.
    Se o operador falhar (sem saída ou ciclo), faz o retrocesso (backtrack).
    """
    inicio_tempo = time.perf_counter()
    nos_visitados = 0

    def backtracking(caminho_atual):
        nonlocal nos_visitados
        nos_visitados += 1
        
        _, estado_atual = caminho_atual[-1]
        
        if estado_atual == estado_meta:
            return caminho_atual
        
        estados_no_caminho = [est for _, est in caminho_atual]
        
        # Testa cada movimento um a um
        for operacao, novo_estado in obter_transicoes(estado_atual):
            if novo_estado not in estados_no_caminho:
                resultado = backtracking(caminho_atual + [(operacao, novo_estado)])
                if resultado is not None:
                    return resultado
                # Retrocesso implícito ocorrendo aqui no loop quando retorna None
        
        return None

    caminho_solucao = backtracking([("raiz", estado_inicial)])
    fim_tempo = time.perf_counter()
    
    if caminho_solucao:
        return {
            "caminho": caminho_solucao,
            "passos": len(caminho_solucao) - 1,
            "nos_visitados": nos_visitados,
            "tempo_ms": (fim_tempo - inicio_tempo) * 1000
        }
    return None


# =============================================================================
# EXIBIÇÃO DE RESULTADOS E IMPRESSÃO FORMATADA
# =============================================================================
def exibir_trajetoria(resultado, titulo):
    """Imprime o resultado detalhado de uma busca."""
    print("=" * 65)
    print(f"  {titulo}")
    print("=" * 65)
    
    if not resultado:
        print("Solução não encontrada.")
        return
        
    caminho = resultado["caminho"]
    print(f"Estado Inicial : {caminho[0][1]} ({formatar_estado(caminho[0][1])})\n")
    
    for i in range(1, len(caminho)):
        op, est = caminho[i]
        print(f"  {i:2d} : {op}  ==>  {est}  ({formatar_estado(est)})")
        
    print(f"\nEstado Final   : {caminho[-1][1]} ({formatar_estado(caminho[-1][1])})")
    print(f"Nro total de passos : {resultado['passos']}")
    print(f"Nós visitados       : {resultado['nos_visitados']}")
    print(f"Tempo de execução   : {resultado['tempo_ms']:.3f} ms\n")


def main():
    print("\n" + "#" * 65)
    print("  ECOI2217 - ATIVIDADE 02: COMPARAÇÃO DE MÉTODOS DE BUSCA")
    print("  Problema: Jogo das Peças Brancas e Pretas")
    print("#" * 65 + "\n")
    
    res_bfs = busca_largura_bfs(ESTADO_INICIAL, ESTADO_META)
    exibir_trajetoria(res_bfs, "METODO DE BUSCA LARGURA PRIMEIRO (BFS)")
    
    res_dfs = busca_profundidade_dfs(ESTADO_INICIAL, ESTADO_META)
    exibir_trajetoria(res_dfs, "METODO DE BUSCA PROFUNDIDADE PRIMEIRO (DFS)")
    
    res_backtrack = busca_backtracking(ESTADO_INICIAL, ESTADO_META)
    exibir_trajetoria(res_backtrack, "METODO DE BUSCA POR BACKTRACKING RECURSIVO")
    
    # Tabela comparativa dos três métodos
    print("=" * 65)
    print("  QUADRO COMPARATIVO DOS RESULTADOS")
    print("=" * 65)
    print(f"{'Método':<25} | {'Passos (Solução)':<16} | {'Nós Visitados':<14} | {'Tempo (ms)':<10}")
    print("-" * 65)
    print(f"{'Busca em Largura (BFS)':<25} | {res_bfs['passos']:<16} | {res_bfs['nos_visitados']:<14} | {res_bfs['tempo_ms']:<10.3f}")
    print(f"{'Busca em Profundidade (DFS)':<25} | {res_dfs['passos']:<16} | {res_dfs['nos_visitados']:<14} | {res_dfs['tempo_ms']:<10.3f}")
    print(f"{'Backtracking Recursivo':<25} | {res_backtrack['passos']:<16} | {res_backtrack['nos_visitados']:<14} | {res_backtrack['tempo_ms']:<10.3f}")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
