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


def insert(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    if value < head.val:
        new_node.next = head
        return new_node

    prev = head
    curr = head.next
    while curr is not None and curr.val < value:
        prev = curr
        curr = curr.next

    prev.next = new_node
    new_node.next = curr
    return head


def remove_max(head):
    if head is None:
        return None

    sentinel_node = Node(None)
    sentinel_node.next = head

    prev = sentinel_node
    curr = head

    max_prev = prev
    max_node = curr

    while curr is not None:
        if curr.val > max_node.val:
            max_node = curr
            max_prev = prev

        prev = curr
        curr = curr.next

    max_prev.next = max_node.next
    return sentinel_node.next


def insertion_sort(head):
    new_head = None

    while head is not None:
        new_head = insert(new_head, head.val)
        head = head.next

    return new_head


arr = [4, 2, 6, 1, 67, 2, 31, 4, 5, 14]
a = to_linked_list(arr)

print_linked_list(a)

# a = insert(a, 19)
# a = insert(a, 14)
# a = insert(a, 1)
# a = insert(a, 13)
#
# print_linked_list(a)

a = insertion_sort(a)

print_linked_list(a)
