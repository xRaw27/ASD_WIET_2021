def tank(S, l, t):
    n = len(S)
    result = []
    curr_fuel = l - S[0]
    for i in range(0, n - 1):
        if S[i] + curr_fuel >= t:
            return result

        if curr_fuel < 0:
            return None

        if curr_fuel - (S[i + 1] - S[i]) < 0:
            result.append(i)
            curr_fuel = l

        curr_fuel -= S[i + 1] - S[i]

    if S[n - 1] + curr_fuel >= t:
        return result

    if S[n - 1] + l >= t:
        result.append(n - 1)
        return result

    return None


arr_s = [5, 7, 9, 11, 13, 19, 22]
res = tank(arr_s, 5, 18)
print(res)
