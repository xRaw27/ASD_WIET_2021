def bubble_sort(T):
    n = len(T)
    for i in range(1, n):
        swapped = False
        for j in range(0, n - i):
            if T[j] > T[j + 1]:
                swapped = True
                T[j], T[j + 1] = T[j + 1], T[j]

        if not swapped:
            return


def insertion_sort(T):
    n = len(T)

    for i in range(1, n):
        j = i
        while j > 0 and T[j] < T[j - 1]:
            T[j], T[j - 1] = T[j - 1], T[j]
            j -= 1


def selection_sort(T):
    n = len(T)

    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if T[j] < T[minimum]:
                minimum = j

        T[i], T[minimum] = T[minimum], T[i]


xd = [4, 2, 6, 1, 67, 2, 31, 4, 5, 14]

# bubble_sort(xd)

# insertion_sort(xd)

selection_sort(xd)

print(xd)
