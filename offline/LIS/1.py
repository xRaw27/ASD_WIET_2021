from time import time


def lis(A):
    t = []
    t_last = []
    t_lengths = []

    for x in A:
        max_len = 0
        for i in range(len(t)):
            if x > t_last[i] and t_lengths[i] > max_len:
                max_len = t_lengths[i]

        if max_len == 0:
            t.append([x])
            t_last.append(x)
            t_lengths.append(1)

        else:
            for i in range(len(t)):
                if x > t_last[i] and t_lengths[i] == max_len:
                    t.append(t[i][:] + [x])
                    t_last.append(x)
                    t_lengths.append(max_len + 1)

    max_len = 0
    for i in range(len(t)):
        if t_lengths[i] > max_len:
            max_len = t_lengths[i]

    count = 0
    for i in range(len(t)):
        if t_lengths[i] == max_len:
            # print(t[i])
            count += 1

    print(count)


# lis([0, 8, 4, 12, 2, 10, 6])
start = time()
# lis([10 * k + i for k in range(8) for i in range(6, 0, -1)])
A = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
lis(A)

print(len(A))
print(A)

print(time() - start)
