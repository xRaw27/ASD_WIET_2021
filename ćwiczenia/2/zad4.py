class Container:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.capacity = (x2 - x1) * (y2 - y1)


def calculate_water(containers, y):
    water = 0
    for container in containers:
        if container.y2 <= y:
            water += container.capacity
        elif container.y1 < y:
            water += (y - container.y1) * container.width

    return water


def water_containers(containers, A):
    T = []
    for container in containers:
        T.append(container.y2)

    T.sort()
    print(T)

    result_height = None
    l = 0
    r = len(T) - 1
    while l < r:
        m = (l + r) // 2
        water = calculate_water(containers, T[m])

        if water == A:
            result_height = T[m]
            break
        elif water > A:
            r = m - 1
        else:
            l = m + 1

    if result_height is None:
        for i in range(l - 1, l + 2):
            if 0 <= i <= len(T) - 1 and calculate_water(containers, T[i]) <= A:
                result_height = T[i]

    # print(result_height)
    result = 0
    for container in containers:
        if container.y2 <= result_height:
            result += 1

    return result


arr = [Container(2, 5, 10, 12), Container(3, 8, 5, 6), Container(6, 12, 0, 2), Container(7, 11, 8, 11),
       Container(12, 14, 4, 10), Container(15, 17, 3, 13), Container(20, 22, 7, 8)]

res = water_containers(arr, 12)

print(res)

# A = [[4, 6, 6, 4], [9, 5, 11, 3], [11, 7, 15, 6], [6, 3, 8, 2]]
# arr = []
# for xd in A:
#     arr.append(Container(xd[0], xd[2], xd[3], xd[1]))
#
# res = water_containers(arr, 13)
#
# print(res)