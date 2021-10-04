from math import inf


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.intervals = []


def print_BST(root, l, r):
    if root is not None:
        left = "-"
        if root.left is not None: left = root.left.key
        right = "-"
        if root.right is not None: right = root.right.key
        parent = None
        if root.parent is not None: parent = root.parent.key

        print("key:", str(root.key).ljust(6, " "), " left:", str(left).ljust(6, " "), " right:",
              str(right).ljust(6, " "), " parent:", str(parent).ljust(6, " "), " interval: ",
              (str(l) + " " + str(r)).ljust(12, " "), "intervals: ", root.intervals)
        print_BST(root.left, l, root.key)
        print_BST(root.right, root.key, r)


def add_nodes(parent, points, l, r):
    m = (l + r) // 2
    new_node = BSTNode(points[m])
    new_node.parent = parent
    if points[m] < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

    if m == l:
        new_node.left = BSTNode(None)
        new_node.left.parent = new_node
    else:
        add_nodes(new_node, points, l, m - 1)

    if m == r:
        new_node.right = BSTNode(None)
        new_node.right.parent = new_node
    else:
        add_nodes(new_node, points, m + 1, r)


def insert_interval(I, interval, root, l, r):
    print(interval, root.key, l, r)
    if interval[0] == l and interval[1] == r:
        root.intervals.append(I)
        return

    if interval[0] < root.key:
        insert_interval(I, (interval[0], min(root.key, interval[1])), root.left, l, root.key)

    if interval[1] > root.key:
        insert_interval(I, (max(root.key, interval[0]), interval[1]), root.right, root.key, r)


# usuwa z drzewa wszystkie przedziały w zadanym przedziale
def remove_intervals(interval, root, l, r):
    print(interval, root.key, l, r)
    if interval[0] == l and interval[1] == r:
        root.intervals = []
        return

    if interval[0] < root.key:
        remove_intervals((interval[0], min(root.key, interval[1])), root.left, l, root.key)

    if interval[1] > root.key:
        remove_intervals((max(root.key, interval[0]), interval[1]), root.right, root.key, r)


def find(root, index):
    result = []
    while True:
        for x in root.intervals:
            result.append(x)
        if root.key is None:
            return result

        if index < root.key:
            root = root.left
        else:
            root = root.right


def build_tree(intervals):
    T = []
    for interval in intervals:
        T.append(interval[0])
        T.append(interval[1])

    T.sort()
    points = []
    for x in T:
        if len(points) == 0 or points[len(points) - 1] != x:
            points.append(x)
    print(points)

    m = (len(points) - 1) // 2
    root = BSTNode(points[m])
    add_nodes(root, points, 0, m - 1)
    add_nodes(root, points, m + 1, len(points) - 1)

    # insert_interval([1, 9, 0], [1, 9], root, -inf, -inf)
    #
    # remove_intervals([1, 9], root, -inf, -inf)
    # insert_interval([1, 3, 1], [1, 3], root, -inf, -inf)
    # insert_interval([3, 9, 0], [3, 9], root, -inf, -inf)
    #
    # remove_intervals([3, 9], root, -inf, -inf)
    # insert_interval([3, 5, 0], [3, 5], root, -inf, -inf)
    # insert_interval([6, 9, 0], [6, 9], root, -inf, -inf)
    # insert_interval([5, 6, 1], [5, 6], root, -inf, -inf)


    for i in range(len(intervals)):
        insert_interval(i, intervals[i], root, -inf, inf)

    print_BST(root, -inf, inf)


# arr = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]
arr = [(1, 3), (5, 6), (4, 7), (6, 9)]
# arr = [(0, 10), (5, 20), (7, 12), (10, 15)]
# arr = [(0, 20), (5, 12), (7, 10), (10, 15)]
build_tree(arr)
