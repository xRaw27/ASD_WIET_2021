# def

def bricks(A):
    n = len(A)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
                F[i] = max(F[i], F[j] + 1)

    print(F)
    return max(F)


# arr = [[1, 5], [2, 7], [3, 4], [1, 10], [3, 3.2]]
arr = [[1, 7], [2, 6], [3, 9], [4, 5]]
print(bricks(arr))
