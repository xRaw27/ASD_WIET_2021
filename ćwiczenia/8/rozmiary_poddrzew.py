def tree_sizes(adj_list, root):
    def DFSVisit(u):
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)
                size[u] += size[v]

    n = len(adj_list)
    visited = [False] * n
    size = [1] * n
    DFSVisit(root)

    print(size)


G = [[1, 7, ],
     [0, 2, 3, 6],
     [1, ],
     [1, 4, 5],
     [3, ],
     [3, ],
     [1, ],
     [0, 8, 9],
     [7, ],
     [7, ]]
tree_sizes(G, 0)
