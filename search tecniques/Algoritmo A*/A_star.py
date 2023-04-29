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

# open file read-only add to dictionary
with open('heuristica_map_romenia.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, valor = linha.strip().split(',')
        heuristica[nome] = int(valor)

# defines the heuristic function that returns the value of the heuristic for a given node
def funcao_heuristica(nodo):
    return heuristica.get(nodo, 0)


def a_star(inicio, destino, grafo):
    # defines the data structures used by the algorithm
    abertos = [(inicio, 0)]
    fechados = set()
    pai = {}
    custo_g = {inicio: 0}  # definition of the cost_g variable
    
    # the priority function with the heuristic
    def prioridade(nodo):
     return custo_g[nodo] + funcao_heuristica(nodo)

    # runs the A* algorithm
    while abertos:
        # gets the lowest priority node from the open list
        atual, _ = min(abertos, key=lambda x: prioridade(x[0]))

        # if the current node is the destination, returns the path
        if atual == destino:
            caminho = [atual]
            while caminho[-1] != inicio:
                caminho.append(pai[caminho[-1]])
            return caminho[::-1]
        
        # removes the current node from the open list and adds it to the closed list
        abertos.remove((atual, _))
        fechados.add(atual)

        # for each node adjacent to the current node, calculates the updated cost
        for adjacente, custo in grafo[atual].items():
            if adjacente in fechados:
                continue
                
            novo_custo = custo_g[atual] + custo
            if adjacente not in [x[0] for x in abertos] or novo_custo < custo_g[adjacente]:
                # atualiza o pai e o custo g do nó adjacente
                pai[adjacente] = atual
                custo_g[adjacente] = novo_custo
                
                # adds the adjacent node to the open list with its priority
                abertos.append((adjacente, prioridade(adjacente)))
    
    # if it doesn't find a path, returns None
    return None


# set the start and destination valuesinicio = 'Zerind'
destino = 'Bucharest'

# starts the A* algorithm
caminho = a_star(inicio, destino, grafo)

# print the result
print(f"Caminho encontrado: {caminho}")
