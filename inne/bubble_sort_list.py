class Node:
    def __init__(self, val, _next):
        self.val = val
        self.next = _next


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


def bucket_sort_list(head):
    guardian = Node("*", head)
    swapped = True
    while swapped:
        p = guardian
        q = p.next
        r = q.next
        swapped = False
        while r is not None:
            if q.val > r.val:
                p.next = r
                q.next = r.next
                r.next = q
                p = r
                r = q.next
                swapped = True
            else:
                p = q
                q = r
                r = r.next

    return guardian.next


t = [5, 1, 2, 8, 12, 5, 10, 7, 4, 2, 0, 6, 9, 2, 1, 3, 7]
l = linked_list(t)
l = bucket_sort_list(l)
print_list(l)

