class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def print_BST(root):
    if root is not None:
        left = None
        if root.left is not None: left = root.left.key
        right = None
        if root.right is not None: right = root.right.key
        parent = None
        if root.parent is not None: parent = root.parent.key

        print("key:", str(root.key).ljust(6, " "), " left:", str(left).ljust(6, " "), " right:", str(right).ljust(6, " "), " parent:", str(parent).ljust(6, " "))
        print_BST(root.left)
        print_BST(root.right)


def next_key(root, key):
    root = find(root, key)

    if root is None:
        return root

    if root.right is not None:
        root = root.right
        while root.left is not None:
            root = root.left

        return root

    while root.parent.key < root.key:
        root = root.parent

    return root.parent



def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None


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
