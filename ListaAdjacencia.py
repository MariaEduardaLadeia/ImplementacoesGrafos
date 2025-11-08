def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)


def remover_vertice(grafo, vertice):
    if vertice in grafo:
        del grafo[vertice]
        for v in grafo:
            if vertice in grafo[v]:
                grafo[v].remove(vertice)


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]


def vizinhos(grafo, vertice):
    return grafo.get(vertice, [])


def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {grafo[vertice]}")
    else:
        print("Vértice não encontrado.")


def grau_vertices(grafo):
    graus = {}
    for v in grafo:
        graus[v] = {"entrada": 0, "saida": len(grafo[v]), "total": 0}
    for origem in grafo:
        for destino in grafo[origem]:
            if destino in graus:
                graus[destino]["entrada"] += 1
    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True


def exibir_grafo(grafo):
    for v in grafo:
        print(f"{v} -> {grafo[v]}")


def main():
    grafo = criar_grafo()
    while True:
        print("\n--- MENU (Lista de Adjacência) ---")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Verificar aresta")
        print("8 - Verificar percurso")
        print("9 - Grau dos vértices")
        op = input("Opção: ")

        if op == "1":
            exibir_grafo(grafo)
        elif op == "2":
            v = input("Vértice: ")
            inserir_vertice(grafo, v)
        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(grafo, o, d, nd)
        elif op == "4":
            v = input("Vértice a remover: ")
            remover_vertice(grafo, v)
        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            remover_aresta(grafo, o, d, nd)
        elif op == "6":
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)
        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(grafo, o, d))
        elif op == "8":
            caminho = input("Percurso (separado por vírgulas): ").split(",")
            print("Percurso válido?", percurso_valido(grafo, caminho))
        elif op == "9":
            graus = grau_vertices(grafo)
            for v, g in graus.items():
                print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")


if __name__ == "__main__":
    main()
