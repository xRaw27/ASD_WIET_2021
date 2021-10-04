def max_interval(intervals):
    n = len(intervals)
    T = []

    for i, interval in enumerate(intervals):
        T.append([interval[0], i, 0])
        T.append([interval[1], i, 1])

    T.sort(key=lambda x: x[0])

    T2 = []
    i = 0
    while i < 2 * n:
        point_info = [T[i][0], [], 0, 0]

        point_info[1].append((T[i][1], T[i][2]))
        if T[i][2] == 0:
            point_info[2] += 1
        else:
            point_info[3] += 1

        while i + 1 < 2 * n and T[i][0] == T[i + 1][0]:
            i += 1

            point_info[1].append((T[i][1], T[i][2]))
            if T[i][2] == 0:
                point_info[2] += 1
            else:
                point_info[3] += 1

        T2.append(point_info)
        i += 1

    T3 = [[x[0], x[1], 0, 0] for x in intervals]

    starts = 0
    ends = 0
    for x in T2:
        ends += x[3]

        for interval_info in x[1]:
            index = interval_info[0]
            if interval_info[1] == 0:
                T3[index][2] = starts + 1
            else:
                T3[index][3] = ends

        starts += x[2]

    print(T)
    print(T2)
    print(T3)

    result = max(T3, key=lambda x: x[3] - x[2])
    return result[0], result[1], result[3] - result[2]


# arr = [[1, 5], [3, 4], [11, 13], [2, 7], [6, 10], [7, 9], [8, 14], [9, 12], [6, 14]]  # (6, 14)
# arr = [[0.9, 4.1], [2, 4], [1, 3], [1, 2], [2, 3]]
# arr = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (4, 7)]  # (4, 7)
arr = [(1, 4), (2, 7), (5, 6), (0, 8), (3, 10)]  # (0, 8)

res = max_interval(arr)

print(res)
