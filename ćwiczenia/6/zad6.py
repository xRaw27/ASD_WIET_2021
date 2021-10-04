def longest_path_in_tree(value, children, root):
    def g(v):
        nonlocal value, children, G

        if len(children[v]) <= 1:
            G[v] = F[v]

        else:
            max_1 = max(F[children[v][0]], F[children[v][1]])
            max_2 = min(F[children[v][0]], F[children[v][1]])

            for i in range(2, len(children[v])):
                if F[children[v][i]] >= max_1:
                    max_2 = max_1
                    max_1 = F[children[v][i]]

                elif F[children[v][i]] > max_2:
                    max_2 = F[children[v][i]]

            G[v] = value[v] + max(max_1, 0) + max(max_2, 0)

    def f(v):
        nonlocal value, children, F

        F[v] = value[v]
        for w in children[v]:
            F[v] = max(F[v], f(w) + value[v])

        g(v)
        return F[v]

    n = len(value)
    F = [0] * n
    G = [0] * n
    f(root)

    print(F)
    print(G)


#        0   1   2  3    4   5   6  7   8  9  10  11  12 13 14  15
_value = [10, 7, -5, 8, -100, 2, -2, 1, -7, 20, 7, -2, -5, 1, 8, -4]
_children = [[1, 2], [3], [4, 5], [6, 7, 8], [], [9, 10], [11], [12], [13], [], [], [14], [15], [], [], []]

longest_path_in_tree(_value, _children, 0)