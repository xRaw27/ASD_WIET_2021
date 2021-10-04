def DFS(adj_list):
    def DFSVisit(u):
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)
        result.append(u)

    n = len(adj_list)
    visited = [False] * n
    result = []
    DFSVisit(9)

    print(result)


G = [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3, 5], [4, 6, 7], [5, 7], [5, 6]]
G2 = [[1, 7], [0, 2, 3, 6], [1], [1, 4, 5], [3], [3], [1], [0, 8, 9], [7], [7]]  # U/U Tree

# DFS(G)
DFS(G2)
