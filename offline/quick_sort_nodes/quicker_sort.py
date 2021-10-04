from random import randint, seed, random
from time import time

seed(123)


class Node:
    def __init__(self, val, n):
        self.val = val
        self.next = n

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


def partition(curr):
    pivot = curr.val

    smaller = Node(None, None)
    p = smaller
    greater = Node(None, None)
    q = greater
    equal = Node(None, None)
    r = equal

    while curr is not None:
        if curr.val < pivot:
            p.next = curr
            p = curr
        elif curr.val > pivot:
            q.next = curr
            q = curr
        else:
            r.next = curr
            r = curr
        curr = curr.next

    p.next = q.next = r.next = None

    return smaller.next, greater.next, equal.next, p, q, r


def quicker_sort(head):
    if head.next is None:
        return head, head

    sm_first, gr_first, eq_first, sm_last, gr_last, eq_last = partition(head)

    if sm_first is not None:
        sm_first, sm_last = quicker_sort(sm_first)
        sm_last.next = eq_first
    else:
        sm_first = eq_first

    if gr_first is not None:
        gr_first, gr_last = quicker_sort(gr_first)
        eq_last.next = gr_first
    else:
        gr_last = eq_last

    return sm_first, gr_last


t = [int(random() * 1000000000) / 100 for _ in range(3000000)]
# t = [randint(-10000000000, 10000000000) for _ in range(0, 1000000)]
l = linked_list(t)

# partition(l)
start = time()
a, b = quicker_sort(l)
print(time() - start)

# print(t)
t.sort()
# print(t)

# print_list(a)
# print_list(b)

print(to_python_list(a) == t)