def hamiltonian_path(adj_list):
    def DFSVisit(u):
        print(u)
        visited[u] = True
        for v in adj_list[u]:
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
    for i in range(len(result) - 1):
        u = result[i]
        v = result[i + 1]
        if v not in adj_list[u]:
            return None

    return result


G = [[1, 2, 5, 6], [3], [5], [4], [2], [6], []]
res = hamiltonian_path(G)
print(res)