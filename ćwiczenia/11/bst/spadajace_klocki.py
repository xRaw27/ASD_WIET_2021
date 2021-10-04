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
    # print(interval, root.key, l, r)
    if interval[0] == l and interval[1] == r:
        root.intervals.append(I)
        return

    if interval[0] < root.key:
        insert_interval(I, (interval[0], min(root.key, interval[1])), root.left, l, root.key)

    if interval[1] > root.key:
        insert_interval(I, (max(root.key, interval[0]), interval[1]), root.right, root.key, r)


# usuwa z drzewa wszystkie przedziały w zadanym przedziale
def remove_intervals(interval, root, l, r):
    # print(interval, root.key, l, r)
    if interval[0] == l and interval[1] == r:
        root.intervals = []
        return

    if interval[0] < root.key:
        remove_intervals((interval[0], min(root.key, interval[1])), root.left, l, root.key)

    if interval[1] > root.key:
        remove_intervals((max(root.key, interval[0]), interval[1]), root.right, root.key, r)


def find(root, index):
    while True:
        if len(root.intervals) > 0:
            return root.intervals[0]

        if root.key is None:
            return None

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
    # print(points)

    m = (len(points) - 1) // 2
    root = BSTNode(points[m])
    add_nodes(root, points, 0, m - 1)
    add_nodes(root, points, m + 1, len(points) - 1)

    return min(points), max(points), root


def falling_blocks(intervals):
    min_key, max_key, root = build_tree(intervals)
    insert_interval([min_key, max_key, 0], [min_key, max_key], root, -inf, inf)

    print_BST(root, -inf, inf)
    print()

    n = len(intervals)
    for i in range(n):
        a = intervals[i][0]
        b = intervals[i][1]
        h = intervals[i][2]

        max_h = 0
        end = a
        last = None
        while end < b:
            curr = find(root, end + 0.5)
            # print(curr)
            max_h = max(max_h, curr[2])
            remove_intervals(curr, root, -inf, inf)

            if curr[0] < a:
                insert_interval([curr[0], a, curr[2]], [curr[0], a], root, -inf, inf)

            end = curr[1]
            last = curr

        if last[1] > b:
            insert_interval([b, last[1], last[2]], [b, last[1]], root, -inf, inf)

        insert_interval([a, b, max_h + h], [a, b], root, -inf, inf)


    print_BST(root, -inf, inf)


falling_blocks([(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)])
# falling_blocks([(1, 3, 1), (2, 5, 2), (4, 6, 1), (4, 5, 1), (0, 8, 2), (8, 9, 3), (4, 6, 2)])

# tu prosze zaimplementowac swoja funkcje
# return [0]*len(I)   # przykladowy bledny wynik


# uruchamia bazowe testy uzywajac funkcji intervals do obliczania wyniku
# wypisuje na koncu "OK!" jesli testy zaliczone
# run_tests(intervals)
