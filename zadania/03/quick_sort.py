from random import randint

def partition(A, p, r):
    x = randint(p, r)
    A[x], A[r] = A[r], A[x]

    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    global counter, counter_max
    counter += 1
    if counter > counter_max:
        counter_max = counter

    if p < r:
        q = partition(A, p, r)

        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

    counter -= 1


def quick_sort_memory_log_n(A, p, r):
    global counter, counter_max
    counter += 1
    if counter > counter_max:
        counter_max = counter

    while p < r:
        q = partition(A, p, r)

        if q - p < r - q:
            quick_sort_memory_log_n(A, p, q - 1)
            p = q + 1
        else:
            quick_sort_memory_log_n(A, q + 1, r)
            r = q - 1

    counter -= 1


A = [randint(-100000, 100000) for _ in range(0, 100000)]
B = A[:]

counter = 0
counter_max = 0
quick_sort(A, 0, len(A) - 1)
print(counter, counter_max)

counter = 0
counter_max = 0
quick_sort_memory_log_n(B, 0, len(B) - 1)
print(counter, counter_max)

# print(A)