from math import log2, floor

def bin_search(T, n, val):
    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2

        if T[m] == val:
            return m

        if val > T[m]:
            l = m + 1
        else:
            r = m - 1

    return -1


def sort(A):
    n = len(A)
    log_n = floor(log2(n))

    print(n, log_n)

    B = [0] * log_n
    C = [0] * log_n

    len_B = 0
    for x in A:
        index = bin_search(B, len_B, x)

        if index >= 0:
            C[index] += 1

        else:
            i = len_B
            B[i] = x
            C[i] = 1
            len_B += 1
            while i > 0 and B[i - 1] > B[i]:
                B[i - 1], B[i] = B[i], B[i - 1]
                C[i - 1], C[i] = C[i], C[i - 1]
                i -= 1

    print(B)
    print(C)

    j = 0
    for i in range(n):
        while C[j] == 0:
            j += 1

        A[i] = B[j]
        C[j] -= 1

    print(A)


arr = [4, 7, 4, 1, 9, 7, 4, 1, 7, 4, 4, 4, 9, 9, 1, 4, 7, 9]
sort(arr)
