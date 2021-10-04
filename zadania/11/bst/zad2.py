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

        print("key:", str(root.key).ljust(6, " "), " left:", str(left).ljust(6, " "), " right:",
              str(right).ljust(6, " "), " parent:", str(parent).ljust(6, " "))
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


def sum_keys(root):
    _sum = 0
    prev_key = None
    while root is not None:
        if prev_key is None:
            _sum += root.key

            if root.left is not None:
                root = root.left

            elif root.right is not None:
                root = root.right

            else:
                print(root.key)
                prev_key = root.key
                root = root.parent

        elif prev_key < root.key and root.right is not None:
            prev_key = None
            root = root.right

        else:
            print(root.key)
            prev_key = root.key
            root = root.parent

    return _sum


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

sum_keys(_root)
