def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def parent(i):
    return (i - 1) // 2


def insert(structure, value):
    min_heap = structure[0]
    max_heap = structure[1]

    min_heap.append([value, 0])
    i = len(min_heap) - 1
    while i > 0:
        j = parent(i)
        if min_heap[j][0] > min_heap[i][0]:
            max_heap[min_heap[j][1]][1] = i
            min_heap[i], min_heap[j] = min_heap[j], min_heap[i]
            i = j
        else:
            break

    max_heap.append([value, i])
    i = len(max_heap) - 1
    while i > 0:
        j = parent(i)
        if max_heap[j][0] < max_heap[i][0]:
            min_heap[max_heap[j][1]][1] = i
            max_heap[i], max_heap[j] = max_heap[j], max_heap[i]
            i = j
        else:
            break

    min_heap[max_heap[i][1]][1] = i
    print(structure)


def remove_min(structure):
    # print(structure)

    min_heap = structure[0]
    max_heap = structure[1]

    n = len(min_heap)

    if n == 0:
        return None

    result = min_heap[0][0]

    i = min_heap[0][1]
    min_heap[max_heap[n - 1][1]][1] = i
    max_heap[i], max_heap[n - 1] = max_heap[n - 1], max_heap[i]
    max_heap.pop()

    max_heap[min_heap[n - 1][1]][1] = 0
    min_heap[0], min_heap[n - 1] = min_heap[n - 1], min_heap[0]
    min_heap.pop()

    # print(structure)
    # print(i)
    # print(0)

    if i < (n - 1):
        while i > 0:
            j = parent(i)
            if max_heap[j][0] < max_heap[i][0]:
                min_heap[max_heap[j][1]][1] = i
                max_heap[i], max_heap[j] = max_heap[j], max_heap[i]
                i = j
            else:
                break
        min_heap[max_heap[i][1]][1] = i

    n -= 1
    i = 0
    while True:
        m = i
        l = left(i)
        r = right(i)
        if l < n and min_heap[l][0] < min_heap[m][0]:
            m = l
        if r < n and min_heap[r][0] < min_heap[m][0]:
            m = r

        if i != m:
            max_heap[min_heap[i][1]][1] = m
            max_heap[min_heap[m][1]][1] = i
            min_heap[i], min_heap[m] = min_heap[m], min_heap[i]
            i = m
        else:
            break

    print(structure)
    return result


xd = [[], []]

insert(xd, 7)
insert(xd, 6)
insert(xd, 2)
insert(xd, 5)
insert(xd, 5)
insert(xd, -1)
insert(xd, 1)
insert(xd, 4)


print(remove_min(xd))
print(remove_min(xd))
print(remove_min(xd))
print(remove_min(xd))
print(remove_min(xd))
print(remove_min(xd))
print(remove_min(xd))

