from math import inf

def decreasing_edges(adj_list, s):
    def DFSVisit(u, last_edge):
        print(u, last_edge, deleted_edges)

        for i in range(deleted_edges[u], len(adj_list[u])):
            v, edge = adj_list[u][i]
            deleted_edges[u] += 1

            if edge == last_edge:
                break

            DFSVisit(v, edge)


    n = len(adj_list)
    deleted_edges = [0] * n
    for a in adj_list:
        a.sort(key=lambda x: x[1])

    print(adj_list)

    DFSVisit(s, inf)


# G = [[(2, 60), (3, 40), (1, 50)], [(0, 50), (4, 49)], [(0, 60), (4, 30), (6, 10), (7, 19)],
#      [(0, 40), (6, 43), (7, 42)], [(1, 49), (2, 30), (6, 45), (5, 20)], [(4, 20)],
#      [(2, 10), (3, 43), (4, 45), (8, 15)], [(3, 42), (2, 19)], [(6, 15)]]
#
# decreasing_edges(G)


