class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.nodes = 0


def print_BST(root):
    if root is not None:
        left = None
        if root.left is not None: left = root.left.key
        right = None
        if root.right is not None: right = root.right.key
        parent = None
        if root.parent is not None: parent = root.parent.key

        print("key:", str(root.key).ljust(6, " "), " left:", str(left).ljust(6, " "), " right:",
              str(right).ljust(6, " "), " parent:", str(parent).ljust(6, " "), " nodes", str(root.nodes).ljust(6, " "))
        print_BST(root.left)
        print_BST(root.right)


def insert(root, key):
    prev_root = root

    while root is not None:
        prev_root = root
        if root.key == key:
            return False
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    new_node = BSTNode(key)
    new_node.parent = prev_root

    if prev_root.key > key:
        prev_root.left = new_node
    else:
        prev_root.right = new_node

    return True


def count_nodes(root):
    if root is None:
        return 0

    root.nodes = 1 + count_nodes(root.left) + count_nodes(root.right)
    return root.nodes


def select(root, i):
    curr_index = root.left.nodes
    while root is not None:
        # print(root.key, curr_index)

        if i == curr_index: return root
        elif i > curr_index:
            root = root.right
            curr_index += 1
            if root.left is not None: curr_index += root.left.nodes
        else:
            root = root.left
            curr_index -= 1
            if root.right is not None: curr_index -= root.right.nodes


def find(root, key):
    curr_index = root.left.nodes
    while root is not None:
        if root.key == key: return curr_index

        elif key < root.key:
            root = root.left
            curr_index -= 1
            if root.right is not None: curr_index -= root.right.nodes
        else:
            root = root.right
            curr_index += 1
            if root.left is not None: curr_index += root.left.nodes

    return None


_root = BSTNode(21)
insert(_root, 15)
insert(_root, 37)
insert(_root, 6)
insert(_root, 40)
insert(_root, 20)
insert(_root, 7)
insert(_root, 13)
insert(_root, 25)
insert(_root, 8)
insert(_root, 70)
insert(_root, 23)
insert(_root, 24)
insert(_root, 30)

count_nodes(_root)

print_BST(_root)

print()
res = select(_root, 3)
print(res.key)

res = find(_root, 13)
print(res)
