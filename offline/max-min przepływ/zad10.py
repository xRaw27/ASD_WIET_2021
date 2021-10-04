from queue import PriorityQueue
from math import inf


def get_path(s, parent, x, result):
    if x == s:
        result.append(s)
        return

    get_path(s, parent, parent[x], result)
    result.append(x)


# funkcja działa podobnie jak algorytm Dijkstry z tą różnicą że z kolejki wyciągamy wierzchołek o największej
# przepustowości oraz relaksacja polega na sprawdzeniu czy nowa przepustowość jest większa od tej wcześniej wyliczonej
def max_extending_path(adj_list, s, t):
    n = len(adj_list)

    capacity = [-inf] * n
    parent = [None] * n
    processed = [False] * n

    queue = PriorityQueue()
    capacity[s] = inf

    # wstawiamy do kolejki wartość capacity ze znakiem minus, ponieważ PriorityQueue w pythonie działa na zasadzie
    # min-heap, więc przechowując wartości przeciwne będzie działało jak max-heap co jest potrzebne w tym algorytmie
    queue.put((-capacity[s], s))

    while not queue.empty():
        u_capacity, u = queue.get()

        # jeśli wierzchołek był już wcześniej przetworzony to pomijamy go
        if processed[u]:
            continue

        # w PriorityQueue przechowuje wartość capacity z minusem zatem mnożymy razy -1 żeby uzyskać rzeczywistą wartość
        u_capacity *= (-1)

        for v, w in adj_list[u]:
            # wyliczamy jaka będzie przepustowość jeśli przejdziemy do wierzchołka v z wierzchołka u
            new_capacity = min(u_capacity, w)

            # jeśli nowa przepustowość jest lepsza niż ta zapisana w tablicy capacity to aktualizujemy ją
            # następnie ustawiamy parenta v na u oraz umieszczamy v w kolejce z zaktualizowaną wartością
            if new_capacity > capacity[v]:
                capacity[v] = new_capacity
                parent[v] = u
                queue.put((-capacity[v], v))

        processed[u] = True

        # jeśli wierzchołek który przetworzyliśmy to wierzchołek końcowy to przerywamy pętle i zwracamy wynik
        if u == t:
            break

    # obliczmy rekurencyjnie ścieżkę na podstawie tablicy parent
    # jeśli ścieżka nie istnieje (np. gdy graf jest niespójny), to zwracamy pustą tablicę
    path = []
    if parent[t] is not None:
        get_path(s, parent, t, path)

    return path


# G = [[(1, 4), (2, 3)],  # 0
#      [(3, 2)],  # 1
#      [(3, 5)],  # 2
#      []]  # 3
#
#
# res = max_extending_path(G, 0, 3)
# print(res)
