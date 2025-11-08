def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        matriz.append([0] * len(vertices))


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        i = vertices.index(vertice)
        vertices.pop(i)
        matriz.pop(i)
        for linha in matriz:
            linha.pop(i)


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    return False


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    viz = []
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            viz.append(vertices[j])
    return viz


def grau_vertices(matriz, vertices):
    graus = {}
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum([linha[i] for linha in matriz])
        graus[v] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print("Vértice não encontrado.")
        return
    viz = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {viz}")


def exibir_grafo(matriz, vertices):
    print("   ", " ".join(vertices))
    for i, linha in enumerate(matriz):
        print(f"{vertices[i]}:", " ".join(str(v) for v in linha))


def main():
    matriz, vertices = criar_grafo()
    while True:
        print("\n--- MENU (Matriz de Adjacência) ---")
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
            exibir_grafo(matriz, vertices)
        elif op == "2":
            v = input("Vértice: ")
            inserir_vertice(matriz, vertices, v)
        elif op == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(matriz, vertices, o, d, nd)
        elif op == "4":
            v = input("Vértice a remover: ")
            remover_vertice(matriz, vertices, v)
        elif op == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("Não direcionado? (s/n): ").lower() == "s"
            remover_aresta(matriz, vertices, o, d, nd)
        elif op == "6":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif op == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(matriz, vertices, o, d))
        elif op == "8":
            caminho = input("Percurso (separado por vírgulas): ").split(",")
            print("Percurso válido?", percurso_valido(matriz, vertices, caminho))
        elif op == "9":
            graus = grau_vertices(matriz, vertices)
            for v, g in graus.items():
                print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")
        

if __name__ == "__main__":
    main()
