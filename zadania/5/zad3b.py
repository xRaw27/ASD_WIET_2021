def bin_search(T, val):
    l = 0
    r = len(T) - 1

    while l <= r:
        m = (l + r) // 2

        if T[m] == val:
            return -1

        if val > T[m]:
            l = m + 1
        else:
            r = m - 1

    return l


def lis_n_log_n(A):
    n = len(A)
    F = []
    B = [-1] * n

    for i in range(n):
        index = bin_search(F, A[i])

        if index >= 0:
            B[i] = index
            if index == len(F):
                F.append(A[i])
            else:
                F[index] = A[i]

    result = []
    curr_len = len(F) - 1
    for i in range(n - 1, -1, -1):
        if B[i] == curr_len:
            result.append(A[i])
            curr_len -= 1

        if curr_len == -1:
            break

    print(F)
    print(B)
    print(len(F), result)


# arr = [7, 1, 7, 8, 5, 6, 12, 4, 3]
arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]

# res = bin_search(arr, 300)
# print(res)
lis_n_log_n(arr)



