def count_connected_components(adj_list):
    def DFSVisit(u):
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)

    n = len(adj_list)
    visited = [False] * n

    result = 0
    for u in range(n):
        if not visited[u]:
            DFSVisit(u)
            result += 1

    print(result)


G = [[1, 2], [0, 3], [0, 3], [1, 2], [], [6, 7], [5, 7], [5, 6]]
G2 = [[1, 7], [0, 2, 3, 6], [1], [1, 4, 5], [3], [3], [1], [0, 8, 9], [7], [7]]  # U/U Tree

# DFS(G)
count_connected_components(G)
