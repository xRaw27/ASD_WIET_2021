from math import inf


def shortest_paths_in_dag(adj_list, s):
    def DFSVisit(u):
        print(u)
        visited[u] = True
        for v, e in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)
        result.append(u)

    n = len(adj_list)
    visited = [False] * n
    result = []

    for u in range(n):
        if not visited[u]:
            DFSVisit(u)

    result.reverse()

    d = [inf] * n
    d[s] = 0
    for u in range(n):
        for v, edge_weight in adj_list[u]:
            if d[u] + edge_weight < d[v]:
                d[v] = d[u] + edge_weight

    return d


G = [[(1, 2), (2, 7)],
     [(2, 4)],
     [(3, 1), (4, 4)],
     [(4, 2)],
     []]
res = shortest_paths_in_dag(G, 0)
print(res)