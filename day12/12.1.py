from collections import deque
with open('12.txt', 'r') as input_str:
    data = input_str.read()


def into_grid(records) -> tuple[list, int, int, int, int]:
    records = [[a for a in b] for b in records.splitlines()]

    for ind_y, y in enumerate(records):
        for ind_x, x in enumerate(y):
            if x.islower():
                records[ind_y][ind_x] = ord(x)
            elif x =="S":
                s_column, s_row = ind_x, ind_y
                records[ind_y][ind_x] = ord('a')
            elif x =="E":
                e_column, e_row = ind_x, ind_y
                records[ind_y][ind_x] = ord('z')

    return (records, s_row, s_column, e_row, e_column)


def shortest_path(records):
    records = [[a for a in b] for b in records.splitlines()]

    for ind_y, y in enumerate(records):
        for ind_x, x in enumerate(y):
            if x.islower():
                records[ind_y][ind_x] = ord(x)
            elif x == 'S':
                start_column, start_row = ind_x, ind_y
                records[ind_y][ind_x] = ord('a')
            elif x == 'E':
                end_column, end_row = ind_x, ind_y
                records[ind_y][ind_x] = ord('z')
    grid = records


    queue = deque()
    queue.append((0, start_row, start_column))
    visited = {(start_row, start_column)}
    while queue:
        print(queue)
        distance, row, column = queue.popleft()
        for next_row, next_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
            if next_row < 0 or next_column < 0 or next_row >= len(grid) or next_column >= len(grid[0]):
                continue
            if grid[next_row][next_column] - grid[row][column] > 1:
                continue
            if (next_row, next_column) in visited:
                continue
            if next_row == end_row and next_column == end_column:
                return distance + 1
            visited.add((next_row, next_column))
            queue.append((distance + 1, next_row, next_column))


print(shortest_path(data))



