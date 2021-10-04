def strongly_connected_components(adj_list):
    def DFSVisit(u):
        nonlocal time
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)

        process_time[u] = time
        time += 1

    def DFSVisit2(u):
        visited[u] = True
        component.append(u)
        for v in adj_list_reversed[u]:
            if not visited[v]:
                DFSVisit2(v)

    def DFSVisit3(u):
        visited[u] = True
        for v in adj_list[u]:
            if vertices_component[u] != vertices_component[v]:
                components_matrix[vertices_component[u]][vertices_component[v]] = 1
            elif not visited[v]:
                DFSVisit3(v)

    n = len(adj_list)
    visited = [False] * n
    process_time = [0] * n
    time = 0
    for u in range(n):
        if not visited[u]:
            DFSVisit(u)

    vertices = [x for x in range(n)]
    vertices.sort(key=process_time.__getitem__)
    vertices.reverse()

    adj_list_reversed = [[] for _ in range(n)]
    for u in range(n):
        for v in adj_list[u]:
            adj_list_reversed[v].append(u)

    visited = [False] * n
    components = []
    for u in vertices:
        if not visited[u]:
            component = []
            DFSVisit2(u)
            components.append(component)

    print(components)

    vertices_component = [0] * n
    for i in range(len(components)):
        for u in components[i]:
            vertices_component[u] = i

    print(vertices_component)
    visited = [False] * n
    components_matrix = [[0] * len(components) for _ in range(len(components))]
    for u in vertices:
        if not visited[u]:
            DFSVisit3(u)

    print()
    [print(x) for x in components_matrix]
    print()

    in_edges = [0] * len(components)
    for row in range(len(components)):
        for col in range(len(components)):
            if components_matrix[row][col] == 1:
                in_edges[col] += 1

    print(in_edges)
    for i, x in enumerate(in_edges):
        if x == 0:
            print(components[i][0])


G = [[5, 9], [4], [9], [2, 8], [7], [2, 10], [1, 8], [6], [2], [3], [0, 1]]
strongly_connected_components(G)

# G2 = [[1, 2],
#       [2, 3],
#       [3, 5],
#       [4, ],
#       [],
#       [],
#       [],
#       [6]]
# strongly_connected_components(G2)