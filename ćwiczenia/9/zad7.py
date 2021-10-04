from queue import PriorityQueue
from math import inf


def gas_stations(fuel_cost, adj_list, d, s, t):
    n = len(adj_list)
    queue = PriorityQueue()

    visited = [[False] * (d + 1) for _ in range(n)]
    cost = [[inf] * (d + 1) for _ in range(n)]
    cost[s][d] = 0

    parent = [[(-1, -1) for _ in range(d + 1)] for _ in range(n)]

    queue.put((0, s, d))

    while not queue.empty():
        _, u, fuel = queue.get()
        # print(u, fuel)

        if visited[u][fuel]:
            continue

        visited[u][fuel] = True

        for v, edge_weight in adj_list[u]:
            # print("\t", v, edge_weight, w[v])
            new_fuel = fuel - edge_weight
            if new_fuel >= 0 and not visited[v][new_fuel] and cost[u][fuel] < cost[v][new_fuel]:
                parent[v][new_fuel] = (u, fuel)
                cost[v][new_fuel] = cost[u][fuel]
                queue.put((cost[v][new_fuel], v, new_fuel))

        if fuel < d:
            if not visited[u][fuel + 1] and cost[u][fuel] + fuel_cost[u] < cost[u][fuel + 1]:
                parent[u][fuel + 1] = (u, fuel)
                cost[u][fuel + 1] = cost[u][fuel] + fuel_cost[u]
                queue.put((cost[u][fuel + 1], u, fuel + 1))

    print(cost)
    print(parent)

    print(cost[t])

    curr_cost = 0
    path = []
    while t != -1:
        path.append((t, curr_cost))
        t, curr_cost = parent[t][curr_cost]

    path.reverse()
    print(path)



G = [[(1, 5), (2, 6), (4, 1)], [(0, 5), (2, 2), (3, 1), (4, 3), (6, 8)], [(0, 6), (1, 2), (3, 3), (5, 4)], [(1, 1), (2, 3), (5, 3)], [(0, 1), (1, 3)], [(2, 4), (3, 3), (6, 3)], [(1, 8), (5, 3), (7, 3)], [(6, 3)]]
arr = [3, 6, 4, 2, 1, 3, 2, 0]
gas_stations(arr, G, 10, 0, 7)
