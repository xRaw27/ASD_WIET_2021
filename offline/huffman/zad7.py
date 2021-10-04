def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def min_heapify(A, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l].val < A[m].val:
        m = l
    if r < n and A[r].val < A[m].val:
        m = r
    if m != i:
        A[m], A[i] = A[i], A[m]  # swap(A[i], A[m])
        min_heapify(A, n, m)


def buildheap(A, n):
    for i in range(parent(n - 1), -1, -1):
        min_heapify(A, n, i)


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.left = l
        self.right = r
        self.index = None


def get_solution(v, code, result):
    # funkcja get solution zapisuje gotowe kody huffmana do tablicy result, funkcja działa rekurencyjnie
    # jeśli idziemy w lewo to dodajemy do kodu "0", a jeśli w prawo to dodajemy "1"
    # kiedy dotrzemy do liścia drzewa to zapisujemy kod w tablicy result pod odpowiednim indeksem
    if v.left is None and v.right is None:
        result[v.index] = code

    if v.left is not None:
        get_solution(v.left, code + "0", result)

    if v.right is not None:
        get_solution(v.right, code + "1", result)


def print_solution(S, F, result, n):
    # funkcja wypisuje kody huffmana mając daną tablicę result oraz tablice wejściowe; obliczana jest także
    # liczba bitów potrzebna do wypisania napisu, w którym każdy symbol występuje podaną częstość razy
    length = 0
    for i in range(n):
        print(S[i], ":", result[i])
        length += F[i] * len(result[i])

    print("dlugosc napisu:", length)


def huffman(S, F):
    # złożoność obliczeniowa: O(nlogn)
    # złożoność pamięciowa: 2n dodatkowej pamięci (2 tablice pomocnicze)
    n = len(F)
    A = [Node(None, None, None)] * n  # tablica do której dodamy node-y, aby zbudować min-heap
    result = [""] * n  # tablica do której zapiszemy kody w tej samej kolejności co dane wejściowe

    # z każdego symbolu tworzymy node-a którego dodajemy do tablicy A
    # zapisujemy index symbolu z tablicy wejściowej, aby potem wyświetlić wynik w odpowiedniej kolejności
    for i in range(n):
        new_node = Node(F[i], None, None)
        new_node.index = i
        A[i] = new_node

    # budujemy min-heap z node-ów
    buildheap(A, n)

    # teraz chcemy połączyć node-y w drzewo potrzebne do utworzenia kodu huffmana dla każdego symbolu
    for i in range(n - 1, 0, -1):
        # wybieramy 2 node-y o najmniejszej częstości, w tym celu bierzemy root kopca, zapisujemy go jako v1 po czym
        # wstawiamy go na koniec kopca i naprawiamy kopiec (ale już bez tego ostatniego elementu) używając heapify
        # drugi pod względem częstości node wybieramy już po prostu jako root kopca ale nie wstawiamy go na koniec
        # bo zamiast tego podmieniamy go na nowego node-a będącego złączeniem tych 2 które wybraliśmy
        # i uruchamiamy jeszcze raz procedurę heapify, aby naprawić kopiec
        v1 = A[0]
        A[0], A[i] = A[i], A[0]
        min_heapify(A, i, 0)
        v2 = A[0]

        A[0] = Node(v1.val + v2.val, v1, v2)
        min_heapify(A, i, 0)

    # po wykonaniu powyższej pętli mamy gotowe drzewo huffmana, teraz wystarczy odczytać wynik
    get_solution(A[0], "", result)
    print_solution(S, F, result, n)


S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]
huffman(S, F)
