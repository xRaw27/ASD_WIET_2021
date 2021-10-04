def tank(S, P, l, t):
    n = len(P)

    stack = []
    next_smaller = [-1] * n
    for i in range(n):
        while len(stack) > 0 and stack[len(stack) - 1][0] > P[i]:
            next_smaller[stack.pop()[1]] = i
        stack.append((P[i], i))

    print(next_smaller)
    print(stack)

    result = []
    curr_fuel = l - S[0]
    for i in range(n - 1):
        if next_smaller[i] != -1 and l >= S[next_smaller[i]] - S[i] > curr_fuel:
            d = S[next_smaller[i]] - S[i]
            result.append((i, d - curr_fuel))
            curr_fuel += d - curr_fuel

        else:
            result.append((i, l - curr_fuel))
            curr_fuel += l - curr_fuel

        curr_fuel -= S[i + 1] - S[i]

    print(result)


arr = [7, 4, 5, 6, 5, 2, 8, 0]
arr_p = [7, 3, 4, 2, 2, 2]
arr_s = [5, 7, 9, 11, 13, 19]
tank(arr_s, arr_p, 6, 22)
