from random import randint, seed
from time import time

class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def list_to_array(A):
    if A is None:
        return []

    res = []
    while A is not None:
        res.append(A.val)
        A = A.next

    return res
def array_to_list(A):
    n = len(A)
    if n == 0:
        return None

    head = Node(A[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(A[i])
        curr = curr.next

    return head


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


def test_sort():
    rr = (-1000, 1000)
    n = 1000000
    m = 1
    print_res = False

    for i in range(m):
        t = [randint(rr[0], rr[1]) for _ in range(n)]
        expected_res = sorted(t)

        if print_res: print('input:   ', t)
        start = time()
        t = list_to_array(quicker_sort(array_to_list(t))[0])
        stop = time()
        if print_res: print('output:  ', t)

        res = 'INCORRECT'
        if t == expected_res:
            res = 'CORRECT'

        print('result:  ', res)
        print('time:    ', stop - start, '\n')

        if res == 'INCORRECT':
            break


test_sort()
