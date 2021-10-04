class Node:
    def __init__(self):
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(edges_list, n):
    edges_list.sort(key=lambda x: x[2])
    vertices = [Node() for _ in range(n)]

    result = []
    for edge in edges_list:
        u = find(vertices[edge[0]])
        v = find(vertices[edge[1]])
        if u != v:
            print(u.parent)
            print(v.parent)

            result.append(edge)
            union(u, v)

    print(result)


# graf reprezentowany jako lista krawędzi
G = [[0, 1, 7], [0, 3, 8], [0, 5, 3], [0, 2, 2], [1, 3, 1], [2, 4, 5], [3, 4, 4], [3, 5, 12], [4, 5, 6]]
V = 6

kruskal(G, V)
