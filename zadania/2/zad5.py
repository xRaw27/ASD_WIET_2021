def leader_of_sequence(A):
    n = len(A)

    leader = A[0]
    counter = 1
    print(leader, counter)

    for i in range(1, n):
        if A[i] == leader:
            counter += 1
        elif counter > 0:
            counter -= 1
        else:
            leader = A[i]
            counter = 1

        print(leader, counter)

    counter = 0
    for i in range(n):
        if A[i] == leader:
            counter += 1

    return counter > (n // 2)


result = leader_of_sequence([2, 5, 2, 2, 6, 2, 4, 5, 2, 4, 2, 2, 2, 5, 6, 4, 1, 1, 2, 2, 2])
print(result)
