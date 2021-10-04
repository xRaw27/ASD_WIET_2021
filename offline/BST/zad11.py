# Implementacja algorytmów dodawania i usuwania węzła w BST przedstawionych na wykładzie.
# Usuwanie elementów opiera się na przepinaniu node-ów, z wyjątkiem przypadku usuwania node-a z dwójką dzieci

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(root, key):
    # w poleceniu jest napisane że funkcja zwraca wartość True lub False, w takim razie musimy założyć
    # że drzewo nie jest puste, bo jeśli drzewo byłoby puste to root = None i nie da się wtedy dodać
    # klucza inaczej niż zwracając wartość nowego node-a, co jest sprzeczne z tym że funkcja zwraca tylko True/False

    prev_root = root
    # najpierw szukamy node-a prev_root do którego dołączymy nowy węzeł
    while root is not None:
        prev_root = root
        if root.key == key:
            # jeśli w BST istnieje już taki klucz zwracamy False
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


def remove(root, key):
    # jeśli BST ma tylko jednego node-a i próbujemy go usunąć to napotkamy problem analogiczny, jak przy próbie
    # wykonania operacji insert na pustym drzewie, zatem musimy założyć że taka sytuacja nie zachodzi

    while root is not None:
        if root.key == key:
            break
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    # jeśli w drzewie nie było danego klucza zwracamy False
    if root is None:
        return False

    # 1 przypadek: usuwany node nie ma dzieci
    if root.left is None and root.right is None:
        if root.parent.key > root.key:
            root.parent.left = None
        else:
            root.parent.right = None

    # 2 przypadek: usuwany node ma tylko prawe dziecko
    elif root.left is None:
        if root.parent is None:
            root.left.parent = None
        elif root.parent.key > key:
            root.parent.left = root.right
            root.right.parent = root.parent
        else:
            root.parent.right = root.right
            root.right.parent = root.parent

    # 3 przypadek: usuwany node ma tylko lewe dziecko
    elif root.right is None:
        if root.parent is None:
            root.left.parent = None
        elif root.parent.key > key:
            root.parent.left = root.left
            root.left.parent = root.parent
        else:
            root.parent.right = root.left
            root.left.parent = root.parent

    # 4 przypadek: usuwany node ma lewe i prawe dziecko
    else:
        _next = root.right
        while _next.left is not None:
            _next = _next.left

        # znaleziony node _next to następnik usuwanego node-a; zamieniamy jego wartość z wartością
        # usuwanego node-a, następnie usuwamy _next tak jak w przypadku 2, bo _next nie ma prawego dziecka
        root.key = _next.key
        _next.right.parent = _next.parent

        if _next.parent.key > key:
            _next.parent.left = _next.right
        else:
            _next.parent.right = _next.right

    return True
