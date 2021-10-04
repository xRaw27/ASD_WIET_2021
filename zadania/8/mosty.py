def print_vertices(adj_list):
    n = len(adj_list)
    for i in range(n):
        print(i, ":", end="  ")
        for x in adj_list[i]:
            print(x, end="  ")
        print()


def bridges(adj_list):
    def DFSVisit(u):
        nonlocal time, adj_list
        time += 1
        d[u] = time
        low[u] = time
        for v in adj_list[u]:
            if d[v] == 0:
                parent[v] = u
                DFSVisit(v)
                if low[v] < low[u]:
                    low[u] = low[v]

            elif d[v] < low[u] and parent[u] != v:
                low[u] = d[v]


        if d[u] == low[u] and parent[u] is not None:
            print("most:", u, parent[u])


    n = len(adj_list)
    d = [0] * n
    low = [0] * n
    parent = [None] * n
    time = 0
    DFSVisit(0)

    print(d)


# G = [[3, 8, 7, 1], [0], [3], [6, 8, 0, 2], [5, 6], [4, 6], [4, 5, 3], [8, 0], [3, 0, 7]]
G = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2, 7], [3, 6], [3, 5], [4]]
# print_vertices(G)
bridges(G)
