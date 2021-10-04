from math import inf
from random import randint
from time import time


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def to_linked_list(T):
    if len(T) == 0:
        return None

    head = Node(T[0])

    p = head
    for i in range(1, len(T)):
        q = Node(T[i])
        p.next = q
        p = q

    return head


def print_linked_list(p):
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next

    print("None")


def merge(p, q):
    result = Node(None)
    curr = result

    while p is not None and q is not None:
        if p.val < q.val:
            curr.next = p
            p = p.next
        else:
            curr.next = q
            q = q.next

        curr = curr.next

    if p is None:
        curr.next = q
    else:
        curr.next = p

    return result.next


def find_increasing_subsequence(head):
    if head is None:
        return None

    prev = head
    curr = head.next
    while curr is not None and prev.val <= curr.val:
        prev = curr
        curr = curr.next

    return prev


def merge_sort(head):
    if head is None:
        return None

    new_head = Node(None)
    new_head.next = head
    head = new_head

    # while find_increasing_subsequence(head.next).next is not None:
    end = False
    while not end:
        end = True
        prev = head
        while True:
            a = prev.next

            p = find_increasing_subsequence(a)
            if p is None:
                break

            q = find_increasing_subsequence(p.next)
            if q is None:
                break

            b = p.next
            curr = q.next

            p.next = None
            q.next = None

            prev.next = merge(a, b)
            end = False

            while prev.next is not None:
                prev = prev.next

            prev.next = curr

    # print_linked_list(head)
    return head.next


arr = [randint(0, 100) for _ in range(0, 30)]

a = to_linked_list(arr)
print_linked_list(a)

# res = find_increasing_subsequence(a)
# print_linked_list(res)

merge_sort(a)

# arr1 = [1, 7, 10, 18]
# arr2 = [2, 5, 12]
# a = to_linked_list(arr1)
# b = to_linked_list(arr2)
#
# res = merge(a, b)
# print_linked_list(res)
