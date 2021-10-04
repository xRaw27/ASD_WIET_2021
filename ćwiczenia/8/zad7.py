from collections import deque

def kings_path(A):

    n = len(A)

    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    d = [[0] * n for _ in range(n)]
    d[0][0] = A[0][0]

    queue = deque()

    queue.append([(0, 0), 1])

    print(queue[0])

    while len(queue) > 0:
        print(queue)
        if queue[0][1] > 1:
            queue.append([queue[0][0], queue[0][1] - 1])
            queue.popleft()
        else:
            u = queue.popleft()[0]

            adjacent = []
            if u[0] > 0: adjacent.append((u[0] - 1, u[1]))
            if u[0] < n - 1: adjacent.append((u[0] + 1, u[1]))
            if u[1] > 0: adjacent.append((u[0], u[1] - 1))
            if u[1] < n - 1: adjacent.append((u[0], u[1] + 1))

            for v in adjacent:
                if not visited[v[0]][v[1]]:
                    visited[v[0]][v[1]] = True
                    d[v[0]][v[1]] = d[u[0]][u[1]] + A[v[0]][v[1]]
                    queue.append([v, A[v[0]][v[1]]])

            # print(adjacent)

    [print(x) for x in visited]
    [print(x) for x in d]


G = [[2, 2, 1, 1],
     [1, 5, 5, 1],
     [5, 5, 5, 1],
     [1, 1, 1, 1]]

kings_path(G)
