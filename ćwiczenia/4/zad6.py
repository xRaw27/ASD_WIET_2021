from random import randint, seed
seed(99)

def min_max(A):
    _min = A[0]
    _max = A[0]
    last_index = len(A) - 1
    for i in range(0, last_index, 2):
        if A[i] > A[i + 1]:
            if A[i] > _max:
                _max = A[i]
            if A[i + 1] < _min:
                _min = A[i + 1]
        else:
            if A[i + 1] > _max:
                _max = A[i + 1]
            if A[i] < _min:
                _min = A[i]

    if A[last_index] > _max:
        _max = A[last_index]
    if A[last_index] < _min:
        _min = A[last_index]

    return _min, _max


def max_difference(A):
    n = len(A)
    _min, _max = min_max(A)
    print(_min, _max)

    buckets = [[] for _ in range(n + 1)]
    bucket_size = (_max - _min) / n

    for x in A:
        index = int((x - _min) / bucket_size)
        buckets[index].append(x)

    print(buckets)
    best = 0
    result = None
    prev_max = None
    for bucket in buckets:
        if len(bucket) > 0:
            curr_min, curr_max = min_max(bucket)

            if prev_max is not None:
                if curr_min - prev_max > best:
                    best = curr_min - prev_max
                    result = (prev_max, curr_min)

            prev_min, prev_max = curr_min, curr_max

    print(result)


arr = [randint(0, 1000) for _ in range(30)]
arr2 = arr[:]
# arr = [0, 1, 2, 4]
print(arr)
max_difference(arr)

arr2.sort()
best = 0
res = None
for i in range(1, len(arr2)):
    if arr2[i] - arr2[i - 1] > best:
        best = arr2[i] - arr2[i - 1]
        res = (arr2[i - 1], arr2[i])
print("XD: ", res)

