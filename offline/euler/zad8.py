from copy import deepcopy
from collections import deque


def is_eulerian(adj_matrix, v):
    # funkcja działa na podstawie BFS i sprawdza czy graf jest spójny oraz czy wierzchołki są stopnia parzystego
    n = len(adj_matrix)

    queue = deque()
    visited = [False] * n
    visited[v] = True

    queue.append(v)
    while len(queue) > 0:
        u = queue.popleft()
        d = 0
        for v in range(n):
            if adj_matrix[u][v] == 1:
                d += 1

            if adj_matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                queue.append(v)

        if d % 2 != 0:
            return False

    for v in visited:
        if not v:
            return False

    return True


def euler(adj_matrix):
    if not is_eulerian(adj_matrix, 0):
        return None

    n = len(adj_matrix)
    stack = []
    euler_cycle = []

    # w tej tablicy będziemy zapisywać ile krawędzi danego wierzchołka jest już przetworzonych, aby nie
    # sprawdzać ich wielokrotnie. Dzięki temu algorytm ma złożoność O(V^2) zamiast O(V^3)
    edges_processed = [0] * n

    # dodajemy 1 wierzchołek na stos
    stack.append(0)

    while len(stack) > 0:
        # pobieramy ze stosu wierzchołek ustawiamy first jako numer 1 nieprzetworzonej krawędzi tego wierzchołka
        i = stack.pop()
        vertex_processed = True
        first = edges_processed[i]

        for e in range(first, n):
            edges_processed[i] += 1
            # iterujemy po krawędziach wierzchołka
            # jeżeli krawędź istnieje czyli w macierzy jest 1 to idziemy tą krawędzią po czym oznaczamy ją jako usuniętą
            if adj_matrix[i][e] == 1:
                # oznaczamy krawędź jako odwiedzoną (usuwamy krawędź)
                adj_matrix[i][e] = adj_matrix[e][i] = 2

                # dodajemy na stack krawędź na której jesteśmy a potem krawędź do której ma pójść teraz DFS
                # następnie przerywamy pętle dzięki czemu w następnej iteracji wykona się ona dla tego następnego
                # wierzchołka (zgodnie z algorytmem DFS) a gdy już go przetworzy wróci do tego
                stack.append(i)
                stack.append(e)

                # znaleźliśmy kolejny wierzchołek na który pójdziemy zatem ten obecny oznaczamy jako nieprzetworzony
                vertex_processed = False
                break

        # kiedy przetworzymy już dany wierzchołek zapisujemy go w cyklu eulera
        if vertex_processed:
            euler_cycle.append(i)

    # przywracamy daną macierz do stanu początkowego
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 2:
                adj_matrix[i][j] = 1

    return euler_cycle


# sprawdzenie czy dla grafu G (o którym zakładamy, że ma cykl Eulera) funkcja zwraca prawidłowy wynik

G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)
# print(cycle)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
