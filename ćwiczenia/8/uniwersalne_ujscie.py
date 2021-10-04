def universal_sink(adj_matrix):
    n = len(adj_matrix)

    col = 0
    row = 0
    while col < n:
        print(row, col)
        if adj_matrix[row][col] == 0:
            col += 1
        else:
            row = col

    for i in range(n):
        if adj_matrix[row][i] != 0 or (i != row and adj_matrix[i][row] != 1):
            return False

    return row


G = [[0, 0, 0, 1, 0],
     [1, 0, 1, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0]]


G2 = [[0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0]]

res = universal_sink(G)
print(res)