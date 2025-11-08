def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        arestas[:] = [a for a in arestas if vertice not in a]


def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    viz = []
    for origem, destino in arestas:
        if origem == vertice:
            viz.append(destino)
    return viz


def grau_vertices(vertices, arestas):
    graus = {v: {"entrada": 0, "saida": 0, "total": 0} for v in vertices}
    for origem, destino in arestas:
        if origem in graus:
            graus[origem]["saida"] += 1
        if destino in graus:
            graus[destino]["entrada"] += 1
    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
    return graus


def percurso_valido(arestas, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    viz = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {viz}")


def exibir_grafo(vertices, arestas):
    print("Vértices:", vertices)
    print("Arestas:")
    for origem, destino in arestas:
        print(f"{origem} -> {destino}")


def main():
    vertices, arestas = criar_grafo()
    while True:
        print("\n--- MENU (Lista de Arestas) ---")
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
            exibir_grafo(vertices, arestas)
        elif op == "2":
            v = input("Vértice: ")
            inserir_vertice(vertices, v)
        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(vertices, arestas, o, d, nd)
        elif op == "4":
            v = input("Vértice a remover: ")
            remover_vertice(vertices, arestas, v)
        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            remover_aresta(arestas, o, d, nd)
        elif op == "6":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(arestas, o, d))
        elif op == "8":
            caminho = input("Percurso (separado por vírgulas): ").split(",")
            print("Percurso válido?", percurso_valido(arestas, caminho))
        elif op == "9":
            graus = grau_vertices(vertices, arestas)
            for v, g in graus.items():
                print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")
       

if __name__ == "__main__":
    main()
