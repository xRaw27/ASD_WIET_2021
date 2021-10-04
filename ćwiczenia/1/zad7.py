from random import randint


def find_sum(T, val):
    i = 0
    j = len(T) - 1

    while i <= j:
        if T[i] + T[j] > val:
            j -= 1
        elif T[i] + T[j] < val:
            i += 1
        else:
            return i, j

    return None


# arr = [1, 7, 18, 21, 22, 23, 29, 31, 32]
# print(is_sum(arr, 36))

t = [randint(0, 100) for _ in range(0, 20)]
t.sort()
print(t)
print(find_sum(t, t[7] + t[10]))
