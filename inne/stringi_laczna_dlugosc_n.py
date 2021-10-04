def counting_sort(A, p, pos):
    q = len(A) - 1
    n = q - p + 1
    # print(n)
    B = [0] * n
    C = [0] * 26

    print(n)

    for i in range(p, q + 1):
        C[ord(A[i][pos]) - 97] += 1

    for i in range(1, 26):
        C[i] += C[i - 1]

    # print(C)
    for i in range(q, p - 1, -1):
        C[ord(A[i][pos]) - 97] -= 1
        B[C[ord(A[i][pos]) - 97]] = A[i]

    for i in range(n):
        A[i + p] = B[i]


def string_sort(A, n):
    k = len(A)
    B = [""]*k
    buckets = [[] for _ in range(n)]
    for i in range(k):
        buckets[len(A[i]) - 1].append(A[i])

    print(buckets)

    p = n
    count = 0
    while count < k:
        q = p - 1
        while len(buckets[q]) == 0:
            q -= 1

        j = k - count - 1
        for x in buckets[q]:
            B[j] = x
            j -= 1

        count += len(buckets[q])
        counting_sort(B, k - count, q)

        print(B, p, q, count, k - count)
        p = q

    for i in range(k):
        A[i] = B[i]


# t = ["safkjhasf", "a",  "abc", 'ab', "abcdefghi", "abc", "fghjk", "dfrgtyu"]
t = ["safkjhasf", "a", "jhgf", "jhgfty", "abc", 'ab', "abcdefghi", "abc", "fghjk", "dfrgtyu", "oiuytrew", "safkjhasf", "a", "jhgf", "jhgfty", "abc", 'ab', "abcdefghi", "abc", "fghjk", "dfrgtyu", "oiuytrew"]
t2 = t[:]

string_sort(t, 114)
print(t)

t2.sort()
print(t2)

# xd = ["", "", "safkjhasf", "dsgehrytj", "abcdefghi"]
#
# counting_sort(xd, 2, 2)
# print(xd)