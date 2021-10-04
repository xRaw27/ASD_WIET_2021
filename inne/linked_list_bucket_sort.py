import random
from time import time

class Node:
    def __init__(self, val, _next):
        self.val = val
        self.next = _next


def add_first(p, val):
    return Node(val, p)


def add_last(curr, val):
    prev = curr
    while curr is not None:
        prev = curr
        curr = curr.next
    prev.next = Node(val, None)


def print_list(p):
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("None")


def linked_list(t):
    l_list = Node(None, None)
    p = l_list
    for val in t:
        p.next = Node(val, None)
        p = p.next
    return l_list.next


def to_python_list(head):
    xd = []
    while head is not None:
        xd.append(head.val)
        head = head.next
    return xd


def merge(p1, p2):
    prev1 = Node(None, p1)
    result = prev1
    curr1 = p1
    curr2 = p2
    while curr2 is not None:
        if curr1 is None or curr1.val >= curr2.val:
            prev1.next = curr2
            prev1 = curr2
            temp = curr2.next
            curr2.next = curr1
            curr2 = temp
        else:
            prev1 = curr1
            curr1 = curr1.next

    return result.next


def find(head):
    if head is None:
        return None

    prev = head
    curr = head.next
    while curr is not None and prev.val <= curr.val:
        prev = curr
        curr = curr.next

    return prev


def mergersort(p):
    while True:
        result = Node(None, None)
        result_last = result
        counter = 0

        while p is not None:
            counter += 1

            first1 = p
            last1 = find(p)

            first2 = last1.next
            if first2 is None:
                result_last.next = p
                break
            last2 = find(first2)

            p = last2.next
            last1.next = None
            last2.next = None

            if last1.val >= last2.val:
                merged_last = last1
            else:
                merged_last = last2

            merged = merge(first1, first2)
            result_last.next = merged
            result_last = merged_last

        p = result.next

        if counter <= 1:
            curr = p
            prev = p
            while curr is not None:
                prev = curr
                curr = curr.next
            return p, prev


def bucket_sort(p):
    curr = p
    _min = p.val
    _max = p.val
    length = 0
    while curr is not None:
        length += 1
        if curr.val > _max:
            _max = curr.val
        elif curr.val < _min:
            _min = curr.val
        curr = curr.next

    buckets = [Node("*", None) for _ in range(length)]
    buckets_last = [buckets[i] for i in range(length)]

    bucket_size = (_max - _min) / length
    curr = p
    while curr is not None:
        index = int((curr.val - _min) / bucket_size)
        if index == length: index -= 1
        buckets_last[index].next = curr
        buckets_last[index] = curr

        temp = curr.next
        curr.next = None
        curr = temp

    # [print_list(p) for p in buckets]

    for i in range(length):
        buckets[i], buckets_last[i] = mergersort(buckets[i].next)

    # print()
    # print()
    # [print_list(p) for p in buckets]

    result = Node("*", None)
    result_last = result
    for i in range(length):
        if buckets[i] is not None:
            result_last.next = buckets[i]
            result_last = buckets_last[i]

    return result.next


# l = Node(12, Node(13, Node(41, Node(3, None))))
# l = linked_list([4.1, 6.4, 2.1, 7.4, 8.1, 3.2, 4.5, 1.1, 10.6, 14.2, 1, 5.1, 4, 3, 3.2, 2.9])
t = [int(random.random() * 1000000000) / 100 for _ in range(3000000)]
t2 = t[:]
t2.sort()
l = linked_list(t)

# print_list(l)
start = time()
l = bucket_sort(l)
print(time() - start)
# print_list(l)
print(to_python_list(l) == t2)
