# Autor Guilherme Pereira Nascimento
# para auxiliar na tradução utilizei software: https://www.deepl.com/pt-BR/translator
# 28/04/2023
#Exercise from Dr.Prof. Camila Bezerra's Artificial Intelligence course

 # creates an empty dictionary for the graph
grafo = {}

with open('grafo_map_romenia.txt', 'r') as arquivo:     # giving the file read-only ('r') and passing alias "arquivo"
    for linha in arquivo: 
        origem, destino, custo = linha.strip().split(',')
        
        if origem not in grafo:     #check if the origin node has not yet been added to the graph.
            grafo[origem] = {}
        if destino not in grafo:    #check if the destination node has not yet been added to the graph.
            grafo[destino] = {}
        
        grafo[origem][destino] = int(custo)
        grafo[destino][origem] = int(custo)     #if the graph is undirected, add the inverse edge as well

print(grafo) 

# creates an empty dictionary for the heuristic function
heuristica = {}

# abre o arquivo somente para leitura adiciona ao dicionário
with open('heuristica_map_romenia.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, valor = linha.strip().split(',')
        heuristica[nome] = int(valor)

# define a função heurística que retorna o valor da heurística para um determinado nó
def funcao_heuristica(nodo):
    return heuristica.get(nodo, 0)


def a_star(inicio, destino, grafo):
    # define as estruturas de dados usadas pelo algoritmo
    abertos = [(inicio, 0)]
    fechados = set()
    pai = {}
    custo_g = {inicio: 0}  # definição da variável custo_g
    
    # define a função de prioridade com a heurística
    def prioridade(nodo):
     return custo_g[nodo] + funcao_heuristica(nodo)

    # executa o algoritmo A*
    while abertos:
        # obtém o nó com menor prioridade da lista de abertos
        atual, _ = min(abertos, key=lambda x: prioridade(x[0]))

        # se o nó atual é o destino, retorna o caminho
        if atual == destino:
            caminho = [atual]
            while caminho[-1] != inicio:
                caminho.append(pai[caminho[-1]])
            return caminho[::-1]
        
        # remove o nó atual da lista de abertos e adiciona na lista de fechados
        abertos.remove((atual, _))
        fechados.add(atual)

        # para cada nó adjacente ao nó atual, calcula o custo atualizado
        for adjacente, custo in grafo[atual].items():
            if adjacente in fechados:
                continue
                
            novo_custo = custo_g[atual] + custo
            if adjacente not in [x[0] for x in abertos] or novo_custo < custo_g[adjacente]:
                # atualiza o pai e o custo g do nó adjacente
                pai[adjacente] = atual
                custo_g[adjacente] = novo_custo
                
                # adiciona o nó adjacente à lista de abertos com sua prioridade
                abertos.append((adjacente, prioridade(adjacente)))
    
    # se não encontrar um caminho, retorna None
    return None



# define os valores de inicio e destino
inicio = 'Zerind'
destino = 'Bucharest'

# executa o algoritmo A*
caminho = a_star(inicio, destino, grafo)

# imprime o resultado
print(f"Caminho encontrado: {caminho}")
