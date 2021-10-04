def bin_search(T, val):
    l = 0
    r = len(T) - 1

    while l <= r:
        m = (l + r) // 2

        if T[m] == val:
            return m

        if val > T[m]:
            l = m + 1
        else:
            r = m - 1

    return None


arr = [1, 7, 18, 21, 22, 23, 29, 31, 32]
print(bin_search(arr, 3333))



# def find_prev(T, val):
#     l = 0
#     r = len(T) - 1
#
#     while l <= r:
#         m = (l + r) // 2
#         if val > T[m]:
#             l = m + 1
#         else:
#             r = m - 1
#
#     return r
