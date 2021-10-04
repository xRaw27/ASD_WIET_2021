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


def reverse(head):
    p = head
    if p is None:
        return None

    q = p.next
    if q is None:
        return head

    r = q.next

    p.next = None
    while r is not None:
        q.next = p
        p = q
        q = r
        r = r.next

    q.next = p
    return q



arr = [2, 1]
a = to_linked_list(arr)

print_linked_list(a)

a = reverse(a)

print_linked_list(a)
