from collections import deque

def BFS(adj_list, visited, color, s):
    queue = deque()
    queue.append(s)
    color[s] = 0

    while len(queue) > 0:
        u = queue.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                color[v] = (color[u] + 1) % 2
                visited[v] = True
                queue.append(v)

            elif color[v] == color[u]:
                return False

    return True


def is_bipartite(adj_list):
    n = len(adj_list)
    visited = [False] * n
    color = [-1] * n
    for u in range(n):
        if not visited[u]:
            if not BFS(adj_list, visited, color, u):
                return False

    print(visited)
    print(color)
    return True


G = [[5, 6], [6, 7], [7], [7], [7, 8], [0], [0, 1], [1, 2, 3, 4], [4]]
res = is_bipartite(G)

print(res)
