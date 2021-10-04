def colors(A, k):
    n = len(A)
    B = [0] * k

    counter = 0
    i = 0
    j = -1
    best = n
    result = None
    while True:
        if counter == k:
            print(i, j)
            if (j - i) < best:
                best = j - i
                result = (i, j)

            B[A[i]] -= 1
            if B[A[i]] == 0:
                counter -= 1
            i += 1
        else:
            j += 1
            if j > (n - 1):
                break

            if B[A[j]] == 0:
                counter += 1
            B[A[j]] += 1

    print(best, result)


arr = [1, 1, 2, 1, 1, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1]
arr2 = [0, 1, 1, 1, 1, 2, 4, 4, 3, 0]
colors(arr, 3)
