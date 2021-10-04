def test(A, value):
    counter = 0
    curr_value = 0
    for i in range(len(A)):
        curr_value += A[i]

        if curr_value >= value:
            counter += 1
            curr_value = 0

    return counter

def max_min(A, k):
    S = sum(A)

    l = 0
    r = S

    while l < r:
        m = (l + r) // 2

        if test(A, m) > k:
            l = m + 1
        else:
            r = m - 1

    print(l, r)


arr = [1, 4, 2, 8, 5, 2, 3, 2]
max_min(arr, 3)
# test(arr, 3, 8)
