from math import *
from random import randint

def partition(A, p, r):
    x = randint(p, r)
    A[r], A[x] = A[x], A[r]

    pivot = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= pivot:
            A[j], A[i + 1] = A[i + 1], A[j]
            i += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p > r - q:
            quick_sort(A, q + 1, r)
            r = q - 1
        else:
            quick_sort(A, p, q - 1)
            p = q + 1


def get_solution(C, F, D, i, j, path, curr):
    # funkcja get solution zapisuje 2 ścieżki do tablicy path
    # funkcja działa rekurencyjnie, w sposób podobny do funkcji tsp, to znaczy:
    # jeśli i < j - 1 to dodajemy do ścieżki path[curr] miasto z indeksem j oraz wywołujemy get_solution dla i=i j=j-1
    # jeśli i == j - 1 to znajdujemy k takie że f(k, j - 1) + d(k, j) jest najmniejsze, dodajemy do ścieżki path[curr]
    # miasto z ind. j, a następnie wywołujemy funkcję rek. dla i=k j=i. musimy teraz uwzględnić to że w tym kolejnym
    # wywołaniu ścieżka która kończyła się na i (była tą krótszą) teraz jest tą kończącą się na j, czyli ścieżki
    # jakby zamieniły się miejscami, dlatego zmieniamy wartość curr z 0->1 lub z 1->0, aby w następnym wywołaniu
    # dodać do odpowiedniej ścieżki
    if j == 0:
        return

    if i == j - 1:
        best = inf
        best_k = 0
        for k in range(j - 1):
            if F[k][j - 1] + D[k][j] < best:
                best = F[k][j - 1] + D[k][j]
                best_k = k

        path[curr].append(C[j][0])
        get_solution(C, F, D, best_k, i, path, (curr + 1) % 2)
    else:
        path[curr].append(C[j][0])
        get_solution(C, F, D, i, j - 1, path, curr)


def print_solution(start, path, result_lenght):
    # funkcja printuje rozwiązanie na podstawie utworzonej przez funkcję get_solution() tablicy path
    print("Długość najkrótszej bitonicznej trasy:", result_lenght)
    print("Trasa:", end=" ")
    print(start, end=" ")

    for i in range(len(path[1]) - 1, -1, -1):
        print(path[1][i], end=" ")

    for i in range(len(path[0])):
        print(path[0][i], end=" ")

    print(start)


def tsp(i, j, F, D):
    # implementacja zależności rekurencyjnej problemu bitonic tsp (funkcja podana na wykładzie)
    if F[i][j] != inf:
        return F[i][j]

    if i == j - 1:
        best = inf
        for k in range(j - 1):
            best = min(best, tsp(k, j - 1, F, D) + D[k][j])
        F[i][j] = best
    else:
        F[i][j] = tsp(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]


def bitonicTSP(C):
    n = len(C)
    F = [[inf] * n for _ in range(n)]
    D = [[0.0] * n for _ in range(n)]

    # sortujemy miasta po współrzędnej x, aby móc utworzyć tablicę D, która w polu D[i[[j] będzie miała
    # zapisaną odległość między i-tym w kolejności, a j-tym w kolejności miastem
    quick_sort(C, 0, n - 1)

    # wyznaczamy odległości między miastami, wypełniając tablicę D, wystarczy wypełnić
    # te pola gdzie j > i, bo tylko do takich pól będziemy odnosić się w funkcji tsp
    for i in range(n):
        for j in range(i + 1, n):
            x = C[j][1] - C[i][1]
            y = C[j][2] - C[i][2]
            D[i][j] = sqrt(x * x + y * y)

    # warunek początkowy rekurencji
    F[0][1] = D[0][1]

    # wyznaczmy najkrótszą trasę poprzez znalezienie minimalnej wartości
    # f(i, n-1) + d(i, n-1) dla i € [0, n - 2] naturalnych, gdzie f(i, j) to minimalny koszt ścieżek 0 -> i, 0->j
    # takich że i < j oraz że łącznie te ścieżki odwiedzają każde miasto ze zbioru {i,...,j} dokładnie raz
    result = [inf, 0]
    for i in range(0, n - 1):
        current = tsp(i, n - 1, F, D) + D[i][n - 1]
        if current < result[0]:
            result[0] = current
            result[1] = i


    # znalezienie ścieżki odpowiadającej znalezionemu wcześniej, optymalnemu i oraz wypisanie jej wraz z długością
    path = [[], []]
    get_solution(C, F, D, result[1], n - 1, path, 1)
    print_solution(C[0][0], path, result[0])


C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]

# C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
#      ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
# C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
#      ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
#      ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]

bitonicTSP(C)
