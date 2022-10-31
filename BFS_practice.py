matrix = [[2, 0, 2, 1, 2],
          [0, 2, 0, 2, 0],
          [2, 2, 2, 2, 1],
          [0, 2, 2, 2, 1],
          [2, 0, 0, 0, 2]]

row, col = (2, 2)
p = 7

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def floodFill(matrix, row, col, p):
    start = matrix[row][col]
    queue = [(row, col)]
    visited = set()
    while len(queue) > 0:
        row, col = queue.pop()
        visited.add((row, col))
        matrix[row][col] = p
        for row, col in neighbours(matrix, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return matrix


def neighbours(matrix, row, col, start):
    for new_row, new_col in directions.values():
        moved_row, moved_col = row + new_row, col + new_col
        if [isValid(matrix, moved_row, moved_col) and matrix[moved_row][moved_col] == start]:
            return (moved_row, moved_col)


def isValid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


floodFill(matrix, row, col, p)
for row in matrix:
    print(*row, sep=" - ")
